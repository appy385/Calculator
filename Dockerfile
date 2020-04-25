FROM python:3
WORKDIR /calculator
ADD . /calculator
CMD [ "python", "calculator.py" ]
