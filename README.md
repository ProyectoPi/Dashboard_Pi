# Estructura del sistema

project/
│── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── admin.py
│   │   ├── supervisor.py
│   │   ├── client.py
│   │   └── visitor.py
│   ├── sockets.py
│   ├── pwa/
│   │   ├── static/
│   │   │   ├── manifest.json
│   │   │   ├── service-worker.js
│   │   │   └── icons/
│   │   └── templates/
│   │       └── base.html
│   └── utils/
│       └── decorators.py
│
├── migrations/
├── tests/
├── requirements.txt
└── run.py

## Componentes del sistema