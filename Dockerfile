FROM python:3.9.16

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install --no-deps numba==0.48

COPY . .

RUN mkdir -p /accordion
RUN mkdir -p /percussion

CMD ["python3", "generate.py", "--samples", "16000", "--wav_out_path", "/accordion/generated_accordion_sound.wav", "logdir/train/final_models/accordion/345000/model.ckpt-345000"]