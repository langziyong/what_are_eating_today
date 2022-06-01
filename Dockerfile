FROM python
RUN pip install flask requests gunicorn
COPY ./ /project/
WORKDIR /project/
CMD gunicorn -w 2 -b 0.0.0.0:8011 app:app