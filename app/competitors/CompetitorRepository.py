from app.repositories.RepositoryGeneric import RepositoryGeneric


class CompetitorRepository(RepositoryGeneric):
    def get_by_name_and_department(self, competitor_name, department):
        return (self.db.query(self.model).filter_by(competitor_name=competitor_name)
                .filter(self.model.competitor_department == department).first())


class ModalityRepository(RepositoryGeneric):
    pass
