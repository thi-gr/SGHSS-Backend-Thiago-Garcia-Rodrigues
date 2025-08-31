# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde

Este projeto é um backend desenvolvido em Django para gerenciamento de pacientes, consultas, receitas e prontuários, com autenticação JWT e controle de acesso por grupos.

## 🚀 Tecnologias

- Python 3.11+
- Django 4.2+
- Django REST Framework
- JWT (SimpleJWT)

## 📦 Instalação

```bash
git clone https://github.com/thi-gr/SGHSS-Backend-Thiago-Garcia-Rodrigues.git
cd sghss
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
