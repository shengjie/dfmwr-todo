FROM python:alpine
RUN pip install flask pymongo
EXPOSE 5000
ENTRYPOINT ["python", "/src/app.py"]
