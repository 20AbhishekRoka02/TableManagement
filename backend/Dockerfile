FROM python:3.11

WORKDIR /code

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]


# FROM node:22

# WORKDIR /tablemanager-ui

# COPY ./frontend/tablemanager-ui/package.json ./tablemanager-ui
# RUN npm install

# COPY ./frontend/tablemanager-ui ./tablemanager-ui

# CMD ["npm","run","dev"]
