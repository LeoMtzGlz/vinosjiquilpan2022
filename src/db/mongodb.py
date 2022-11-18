
import pymongo

class PyMongo():
    def __init__(self,variables): #host='localhost', db='opensource', port=27017, timeout=1000, user='', password=''
        self.MONGO_DATABASE = variables["db"]
        self.MONGO_URI = 'mongodb://' + variables["host"] + ':' + str(variables["port"])
        #self.MONGO_URI = 'mongodb+srv://user-itj:enter@cluster0.psya2bm.mongodb.net/?retryWrites=true&w=majority'
        self.MONGO_CLIENT =None
        self.MONGO_RESPUESTA = None
        self.MONGO_TIMEOUT = variables["timeout"]

    def conectar_mongodb(self):
        try:
            self.MONGO_CLIENT = pymongo.MongoClient(self.MONGO_URI, serverSelectionTimeoutMS=self.MONGO_TIMEOUT)
        except Exception as error:
            print("ERROR", error)
        else:
            pass
            # print("Conexión al servidor de MongoDB realizada: ", )
        # finally:


    def desconectar_mongodb(self):
        if self.MONGO_CLIENT:
            self.MONGO_CLIENT.close()

    def consulta_mongodb(self,tabla, filtro, atributos={"_id":0}):
        response = {"status": False, "resultado":[]}
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].find(filtro, atributos)
        if self.MONGO_RESPUESTA:
            response["status"] = True
            for reg in self.MONGO_RESPUESTA:
                response["resultado"].append(reg)
        return response


    # Insertar datos en la coleccion de estudiantes
    def insertar(self, tabla, documento):
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].insert_one(documento)
        if self.MONGO_RESPUESTA:
            return self.MONGO_RESPUESTA
        else:
            return None

    # Actualizar documentos en las colecciones
    def actualizar(self, tabla, filtro, nuevos_valores):
        response ={"status": False}
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].update_many(filtro,nuevos_valores)
        if self.MONGO_RESPUESTA:
            response["status"] = True
            # return self.MONGO_RESPUESTA
        # else:
        #     return None
        return response

    # Obtener el promedio de estudiantes
    def obtener_promedios(self,tabla):
        response = {"status": False, "resultado": []}
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].aggregate(
                                  [
                                    {
                                      "$group":
                                      {
                                        "_id": "$control",
                                        "promedio": { "$avg": "$calificacion" }
                                      }
                                    }
                                  ]
                                )
        if self.MONGO_RESPUESTA:
            response["status"] = True
            for reg in self.MONGO_RESPUESTA:
                response["resultado"].append(reg)
        return response

    # Eliminar documentos en las colecciones
    def eliminar(self, tabla, filtro):
        response = {"status": False}
        self.MONGO_RESPUESTA = self.MONGO_CLIENT[self.MONGO_DATABASE][tabla].delete_many(filtro)
        if self.MONGO_RESPUESTA:
            response["status"] = True
        return response