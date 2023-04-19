## MongoDB Client ##

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Iniciar servicio: net start MongoDB
# Detener servicio: net stop MongoDB
# Extensión: MongoDB for VS Code
# Conexión: mongodb://localhost

from pymongo import MongoClient


# Base de datos local
# db_client = MongoClient().local

# Base de datos remota

# MongoDB Atlas

# FastAPI Cluster
db_client = MongoClient(
    "mongodb+srv://davld7:<password>@cluster0.lqkfpjl.mongodb.net/?retryWrites=true&w=majority").fastapi
