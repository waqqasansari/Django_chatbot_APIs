from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class Chatbot:
    def __init__(self, model_name='microsoft/DialoGPT-large', temperature=0.7):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.temperature = temperature
        self.chat_history_ids = None

    def generate_response(self, input_text, max_length=100):
        input_ids = self.tokenizer.encode(str(input_text) + self.tokenizer.eos_token, return_tensors='pt')

        # Append tokens to chat history
        bot_input_ids = torch.cat([self.chat_history_ids, input_ids], dim=-1) if self.chat_history_ids is not None else input_ids

        # Generate a response
        self.chat_history_ids = self.model.generate(
            bot_input_ids,
            max_length=max_length,
            pad_token_id = self.tokenizer.eos_token_id,
            temperature=self.temperature,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            top_k=50,
            top_p=0.95
        )

        # Decode and return the response as a string
        response_text = self.tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response_text