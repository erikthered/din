A Python web service using Falcon. Accepts a JSON body in a HTTP POST which is then read by the Festival TTS engine.

Request body:

```
{
	"text": "Message to speak",
	"stretchFactor": 1.0
}
```

* _text_: the message to speak
* _stretchFactor_: float between 0.0 and 5.0. 1.0 is normal speed, 5.0 is slowest and 0.0 is fastest.

## Requirements

This really only works on Debian/Ubuntu right now.

python3
pip
virtualenv
festival
festival-dev

## Background

A silly toy to have fun with our team's Raspberry Pi.

## Usage

Start with ```gunicorn din:app```