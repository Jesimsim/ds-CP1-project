
def Summrizer(text, model_path='./model'):
    """
    학습된 모델을 통해 요약문을 도출하는 함수입니다
    model_path = 기본 './model'
    """
    import torch
    from transformers import PreTrainedTokenizerFast
    from transformers import BartForConditionalGeneration
    model = BartForConditionalGeneration.from_pretrained(model_path)
    tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-summarization')

    raw_input_ids = tokenizer.encode(text)
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]

    summary_ids = model.generate(torch.tensor([input_ids]),  num_beams=4,  max_length=128,  eos_token_id=1)
    summary = tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)

    return summary