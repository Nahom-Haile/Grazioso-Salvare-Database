from pymongo import MongoClient
from pymongo.errors import PyMongoError

class AnimalShelter:
    """CRUD operations for the animal collection in MongoDB."""

    def __init__(
        self,
        username,
        password,
        database_name="aac",
        collection_name="animals"
    ):
        
        """Initialize the MongoDB connection."""
        
        host = "localhost"
        port = 27017
        
        #Connect to MongoDB and authenticate through the admin database.
        self.client = MongoClient(
            host=host,
            port=port,
            username=username,
            password=password,
            authSource="aac"
        )
        
        #Store references to the specified database and collection.
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    """Insert a document into the collection."""
    
    def create(self, data):

        if not isinstance(data, dict) or not data:
            return False

        try:
            result = self.collection.insert_one(data)
            return result.inserted_id is not None

        except PyMongoError as error:
            print("Create error:", error)
            return False
        
    """Find documents that match a query."""
    
    def read(self, query):

        if not isinstance(query, dict):
            return []

        try:
            #find() returns a MongoDB cursor.
            cursor = self.collection.find(query)

            return list(cursor)

        except PyMongoError as error:
            print("Read error:", error)
            return []
        
    """Update documents that match a query."""
    
    def update(self, query, update_data):

        if not isinstance(query, dict) or not isinstance(update_data, dict):
            return 0

        try:
            result = self.collection.update_many(
                query,
                update_data
            )

            return result.modified_count

        except PyMongoError as error:
            print("Update error:", error)
            return 0
        
    """Delete documents that match a query."""
    
    def delete(self, query):

        if not isinstance(query, dict):
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count

        except PyMongoError as error:
            print("Delete error:", error)
            return 0