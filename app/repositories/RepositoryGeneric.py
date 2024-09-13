from app.core.exceptions import NotFoundError
from app.utils.Utilities import Utilities


class RepositoryGeneric:
    def _init_(self, model, db):
        self.model = model
        self.db = db

    def add(self, entity, user_token=""):
        entity.created_at = Utilities.get_current_time()
        entity.created_by = user_token
        self.db.add(entity)
        return entity

    def get_by_id(self, id, id_column='id', raise_exception=True):
        data = self.db.query(self.model).filter_by(**{id_column: id}).filter(self.model.status == 1).first()
        if data is None and raise_exception:
            raise NotFoundError(f"Not found {id} in colum id {id_column} in model {self.model}")
        return data

    def get_all(self):
        return self.db.query(self.model).filter(self.model.status == 1).all()

    def get_all_filter_cc_by_ids(self, list_of_cc_ids):
        print("Filter List By CC")
        return self.db.query(self.model).filter(
            self.model.status == 1,
            self.model.cc_id.in_(list_of_cc_ids)
        ).all()

    def update(self, entity):
        # self.db.commit()
        return entity

    def delete(self, id):
        entity = self.db.query(self.model).filter_by(id=id).first()
        self.db.delete(entity)
        # self.db.commit()

    def get_all_by_id(self, id, id_column='id'):
        return self.db.query(self.model).filter_by(**{id_column: id}).filter(self.model.status == 1).all()

    def delete_by_id(self, id, id_column='id'):
        data = self.db.query(self.model).filter_by(**{id_column: id}).filter(self.model.status == 1).first()
        self.db.delete(data)
        return data