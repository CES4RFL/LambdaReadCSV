FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN  yum -y install gcc python-setuptools python-devel postgresql-devel
RUN  pip install --upgrade pip 
RUN python -m pip install -r requirements.txt

COPY . ${LAMBDA_TASK_ROOT}

CMD [ "main.handler_name" ]
