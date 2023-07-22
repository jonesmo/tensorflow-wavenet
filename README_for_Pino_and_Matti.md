# Generating Audio with Your Trained Models

Hi Pino and Matti and future TaPIR folks!  Here are some instructions for how to generate audio snippets using the trained neural networks (known henceforth as "models").  If you run into troubles (not unlikely), email me at mojones.e@gmail.com.  I'm glad to talk through it with you.

## Clone the Repository

For instructions on how to clone this repository to your local machine, [see GitHub's documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

## Guide to the Models

If you look in the folder logdir/train/final_models, you'll find an accordion folder and a percussion folder.  Each of these contains two folders with numeric names (92150 and 345000 for accordion, 280550 and 299999 for percussion).  In turn, each of these contains three files that start with model.ckpt-...  You don't have to worry about the model.ckpt files or open them; they are the weights of the models themselves.

The numeric names of the folders are the number of training steps that completed before that version of the model was saved.  I trained each model through ~400,000 training steps, and I saved them at various points along the way and tested them out to see what they sounded like.  I'm providing two models at different phases of training for each instrument because they generate slightly different kinds of sounds, and I wanted you to have the chance to play with both a more-trained and a less-trained model.

## Using the Dockerized Models

I packaged up the models into something called [Docker containers](https://www.docker.com/resources/what-container/).  These will allow you to run the models and generate audio anytime, anywhere, as long as you have Docker installed on your computer.

First, you'll need to install the version of [Docker Desktop](https://www.docker.com/products/docker-desktop/) appropriate for your machine (pay attention to whether you have an Intel or M1 chip if you're on a Mac).  Once you have it installed, make sure Docker is running.

Next, open a terminal (on your computer or within VSCode, if you're familiar with that) and navigate to the root of this *tensorflow-wavenet* repository, where this README is located.  If you'd like to learn how to navigate your computer using a terminal, there's a [decent tutorial here](https://terminalcheatsheet.com/guides/navigate-terminal#lets-get-started).

In the terminal, once you're inside the repository, build the docker image:
`docker build --tag audiogen .`
Don't forget the . at the end!
This will take a while.

Run the model to generate a one-second clip of audio:
`docker run --rm -v ./generated_audio:/generated audiogen --samples 16000 --wav_out_path "/generated/generated_sound.wav" "logdir/train/final_models/accordion/345000/model.ckpt-345000"`

This will create a new folder called *generated_audio* on your machine, inside this repository.
After this step is done running, *generated_audio* should contain an audio file.  Hooray!

The general formula for this command is:
`docker run --rm -v ./generated_audio:/generated audiogen --samples 16000 --wav_out_path "/generated/<your_preferred_filename>.wav" "logdir/train/final_models/<accordion_or_percussion>/<model_number>/model.ckpt-<model_number>"`

You can fill in `<your_preferred_filename>`, `<accordion_or_percussion>`, and `<model_number>` as you like.  For example, if you want to generate an accordion sound, fill in `accordion` and either `92150` or `345000` in the above command, plus your preferred filename.

You can rename and move the newly-generated audio file to your preferred location.  If you don't move or rename the file and you run the script again with the same `your_preferred_filename`, the file will be overwritten.

If you want to generate a longer audio file, you can replace `16000` in the above command with a larger number.  The audio is generated at a sample rate of 16kHz, so if you want two seconds of audio, you can specify `32000` samples (16000 * 2), and if you want three seconds of audio, you can specify `48000` samples (16000 * 3), etc.

Some of the sounds you generate are likely to sound bad.  Some will sound good!  You might get a bunch of audio files that sound almost exactly the same.  Play around with it!  When I wrote *approximations* using the output of these models, I wrote code that stitched together the best-sounding one- to four-second clips into longer textures.  Feel free to manipulate the sounds however you want.  

Thanks for giving these a try, and I'd be happy to hear whatever you make with them!  My email is above if you'd like to share or to ask questions.

## Acknowledgements and Copyright

These models were trained exclusively on recordings of solo improvisations by percussionist Louis Pino and accordionist Matti Pulkki.  Their development was supported by the University of Toronto's TaPIR Lab, the Social Sciences and Humanities Research Council of Canada, and Spantree Technology Group, LLC.  All audio generated by these models is owned in equal parts by Molly Jones, TaPIR Lab c/o Aiyun Huang, Louis Pino, and Matti Pulkki, all rights reserved.  If you'd like to publish a piece using audio you've generated with these models, please get in touch with us!  mojones.e@gmail.com, uofttapir@gmail.com

## DEPRECATED: The below is no longer true, keeping it for future reference
<!-- To download our generated sound to local, we have to mount a dummy container to the volume and pull out the contents.

```bash
docker run -d --rm --name dummy -v generated_audio:/generated alpine tail -f /dev/null
docker cp dummy:/generated_audio/generated_percussion_299999.wav /Users/mollyejones/Music/TaPIR_lab_2022_23/tensorflow-wavenet-v2/generated_audio
docker stop dummy
```
-->