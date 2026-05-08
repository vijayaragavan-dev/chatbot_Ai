"""
chatbot.py

Offline AI chatbot using TinyLlama chat model.
Designed for cleaner, more professional, beginner-friendly responses.
"""

from typing import Dict, List, Tuple

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


# -----------------------------
# Configuration
# -----------------------------
PRIMARY_MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
FALLBACK_MODEL_NAME = "microsoft/DialoGPT-small"

MAX_HISTORY_MESSAGES = 8
MAX_HISTORY_TOKENS = 900
MAX_NEW_TOKENS = 160

# Generation settings tuned for helpful and stable outputs
DO_SAMPLE = True
TOP_K = 40
TOP_P = 0.9
TEMPERATURE = 0.45
REPETITION_PENALTY = 1.15
NO_REPEAT_NGRAM_SIZE = 3

EXIT_COMMANDS = {"exit", "quit"}


def print_banner() -> None:
    """Print startup banner and usage instructions."""
    print("=" * 74)
    print("chatbot_ai - Offline AI Chatbot (TinyLlama Chat)")
    print("=" * 74)
    print("Type your message and press Enter.")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("Press Ctrl+C to stop safely.")
    print("-" * 74)


def load_tokenizer_and_model() -> Tuple[AutoTokenizer, AutoModelForCausalLM, str]:
    """
    Load tokenizer and model, with a fallback model option.

    Returns:
        Tuple[tokenizer, model, active_model_name]

    Raises:
        RuntimeError: If all model loading attempts fail.
    """
    load_errors: List[str] = []

    for model_name in (PRIMARY_MODEL_NAME, FALLBACK_MODEL_NAME):
        try:
            print(f"Loading model: {model_name} (first run may take time)...")
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForCausalLM.from_pretrained(model_name)

            # Ensure pad token is defined for safe generation
            if tokenizer.pad_token_id is None:
                tokenizer.pad_token = tokenizer.eos_token

            print(f"Model loaded successfully: {model_name}")
            return tokenizer, model, model_name
        except Exception as exc:
            load_errors.append(f"{model_name}: {exc}")
            print(f"Could not load {model_name}. Trying fallback...")

    raise RuntimeError("Failed to load models:\n" + "\n".join(load_errors))


def build_chat_messages(history: List[Dict[str, str]], user_text: str) -> List[Dict[str, str]]:
    """
    Build chat messages list including system instruction.

    Args:
        history: Prior conversation messages in chat-template format.
        user_text: Current user message.

    Returns:
        Message list containing system, recent history, and current user message.
    """
    system_message = {
        "role": "system",
        "content": (
            "You are a professional, beginner-friendly coding assistant. "
            "Answer clearly, accurately, and in an educational tone. "
            "Avoid slang, memes, and casual internet style."
        ),
    }

    recent_history = history[-MAX_HISTORY_MESSAGES:]
    messages = [system_message] + recent_history + [{"role": "user", "content": user_text}]
    return messages


def encode_messages(
    tokenizer: AutoTokenizer,
    messages: List[Dict[str, str]],
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Convert chat messages to token IDs and attention mask.

    Args:
        tokenizer: Loaded model tokenizer.
        messages: Chat-template formatted messages.

    Returns:
        Tuple[input_ids, attention_mask]
    """
    # Use model chat template when available; otherwise build plain text prompt
    try:
        prompt_text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
    except Exception:
        plain_lines = []
        for message in messages:
            role = message.get("role", "user").capitalize()
            content = message.get("content", "")
            plain_lines.append(f"{role}: {content}")
        plain_lines.append("Assistant:")
        prompt_text = "\n".join(plain_lines)

    encoded = tokenizer(
        prompt_text,
        return_tensors="pt",
        truncation=True,
        max_length=MAX_HISTORY_TOKENS,
        padding=False,
    )

    input_ids = encoded["input_ids"]
    attention_mask = encoded["attention_mask"]
    return input_ids, attention_mask


def generate_response_ids(
    model: AutoModelForCausalLM,
    tokenizer: AutoTokenizer,
    input_ids: torch.Tensor,
    attention_mask: torch.Tensor,
) -> torch.Tensor:
    """
    Generate response token IDs from model.

    Args:
        model: Loaded Causal LM model.
        tokenizer: Loaded tokenizer.
        input_ids: Prompt tokens.
        attention_mask: Prompt attention mask.

    Returns:
        Newly generated response token IDs.

    Raises:
        RuntimeError: If generation fails.
    """
    try:
        output_ids = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=DO_SAMPLE,
            top_k=TOP_K,
            top_p=TOP_P,
            temperature=TEMPERATURE,
            repetition_penalty=REPETITION_PENALTY,
            no_repeat_ngram_size=NO_REPEAT_NGRAM_SIZE,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )
        return output_ids[:, input_ids.shape[-1] :]
    except Exception as exc:
        raise RuntimeError(f"Model generation failed: {exc}") from exc


def decode_response(tokenizer: AutoTokenizer, response_ids: torch.Tensor) -> str:
    """
    Decode model response tokens into readable text.

    Args:
        tokenizer: Loaded tokenizer.
        response_ids: Generated response token IDs.

    Returns:
        Clean chatbot response text.
    """
    if response_ids is None or response_ids.shape[-1] == 0:
        return "I could not generate a response. Please try rephrasing your question."

    text = tokenizer.decode(response_ids[0], skip_special_tokens=True).strip()
    if not text:
        return "I could not generate a clear response. Please try again."
    return text


def update_history(history: List[Dict[str, str]], user_text: str, assistant_text: str) -> List[Dict[str, str]]:
    """
    Append new user/assistant turns and keep rolling history.

    Args:
        history: Existing chat history.
        user_text: User message.
        assistant_text: Assistant response.

    Returns:
        Updated history list.
    """
    history.append({"role": "user", "content": user_text})
    history.append({"role": "assistant", "content": assistant_text})

    if len(history) > MAX_HISTORY_MESSAGES:
        history = history[-MAX_HISTORY_MESSAGES:]
    return history


def run_chat_loop(model: AutoModelForCausalLM, tokenizer: AutoTokenizer) -> None:
    """Run the interactive chatbot loop."""
    history: List[Dict[str, str]] = []

    while True:
        try:
            user_text = input("You: ").strip()

            # Safe exit
            if user_text.lower() in EXIT_COMMANDS:
                print("Chatbot: Goodbye! Thanks for chatting.")
                break

            # Friendly empty-input handling
            if not user_text:
                print("Chatbot: Please type a message or 'exit' to quit.")
                print("-" * 74)
                continue

            # Build prompt messages and tokenize with explicit attention mask
            messages = build_chat_messages(history, user_text)
            input_ids, attention_mask = encode_messages(tokenizer, messages)

            # Generate and decode response
            response_ids = generate_response_ids(model, tokenizer, input_ids, attention_mask)
            response_text = decode_response(tokenizer, response_ids)

            print(f"Chatbot: {response_text}")
            print("-" * 74)

            # Update rolling history
            history = update_history(history, user_text, response_text)

        except KeyboardInterrupt:
            print("\nChatbot: Session interrupted. Exiting safely.")
            break
        except RuntimeError as exc:
            print(f"Chatbot: {exc}")
            print("Chatbot: Please try again with a shorter message.")
            print("-" * 74)
        except Exception as exc:
            print(f"Chatbot: Unexpected error: {exc}")
            print("Chatbot: Please retry your message.")
            print("-" * 74)


def main() -> None:
    """Program entry point."""
    print_banner()
    try:
        tokenizer, model, active_model = load_tokenizer_and_model()
        print(f"Using model: {active_model}")
        print("-" * 74)
        run_chat_loop(model, tokenizer)
    except KeyboardInterrupt:
        print("\nChatbot: Startup interrupted. Goodbye.")
    except Exception as exc:
        print(f"Chatbot: Failed to start: {exc}")


if __name__ == "__main__":
    main()
