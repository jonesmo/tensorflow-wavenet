# Generating Audio with Your Trained Models

Hi Pino and Matti!  Here are some instructions for how to generate audio snippets using the trained neural networks (known henceforth as "models").

## Guide to the Models

If you look in the folder logdir/train/final_models, you'll find an accordion folder and a percussion folder.  Each of these contains two further folders with numeric names (92150 and 345000 for accordion, 280550 and 299999 for percussion).  In turn, each of these contains three files that start with model.ckpt-...  You don't have to worry about the model.ckpt files or open them; they are the program files that implement the models.  The numeric names of the folders are the number of training steps that had completed before that version of the model was saved.  Basically, I trained each model through ~400,000 training steps, and I saved them at various points along the way and tested them out to see what they sounded like.  I'm giving you each two models at different phases of training because they generate slightly different kinds of sounds, and I wanted you to have the chance to play with both.

## Installing Stuff
Before you generate any sounds, you have to install a couple programs onto your machine.  To run the installation, go to your Terminal and type

```bash
pip install -r requirements.txt
```

and press enter.  Then wait for the installation to complete.

If you get an error message that says something like
```bash
pip: command not found
```
that means you need to install pip onto your machine before you do the other installation.  I can walk you through this.

## Generating Sounds
Once the installation is done, you can start generating sounds.  In your Terminal, you'll type:

```bash
python3 generate.py —samples 16000 —wav_out_path <provide a file path and file name on your local machine where you'd like to save the sound> <provide file path to model you’d like to use to train>
```

For example, for percussion:
```bash
python3 generate.py --samples 16000 --wav_out_path /Users/mollyejones/Music/TaPIR_lab_2022_23/tensorflow-wavenet-v2/logdir/generated_audio/percussion/generated_percussion_sound.wav logdir/train/final_models/percussion/299999/model.ckpt-299999
```

For example, for accordion:
```bash
python3 generate.py --samples 16000 --wav_out_path /Users/mollyejones/Music/TaPIR_lab_2022_23/tensorflow-wavenet-v2/logdir/generated_audio/accordion/generated_accordion_sound.wav logdir/train/final_models/accordion/345000/model.ckpt-345000
```

The neural networks produce audio at a sample rate of 16 kHz.  This means that the above commands generate one second of sound.  If you want to generate, say, two seconds of sound, you'd replace
```bash
--samples 16000
```
in the above commands with
```bash
--samples 32000
```

Sometimes generating longer stretches of sound yields interesting results, and sometimes it doesn't.

If you feel comfortable with this and want to try out other models to get more variety of sounds, dig through logdir/train/accordion and logdir/train/percussion.  The numbered folders in there all contain models at different stages of training, and they all produce sounds that are a bit different.  Most of them will produce noise or garbage some of the time.  Feel free to dig through and try them out!