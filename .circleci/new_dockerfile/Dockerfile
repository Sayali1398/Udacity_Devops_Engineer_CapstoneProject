FROM python:3.7.3-stretch
WORKDIR /test
COPY . app1.py /test/
## Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&pip install -U Flask


## Step 4:
# Expose port 80
EXPOSE 90

## Step 5:
# Run app.py at container launch
CMD ["python","app1.py"]
