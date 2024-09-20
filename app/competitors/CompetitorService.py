import uuid

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.competitors.CompetitorModel import CompetitorsEntity, ModalitiesEntity
from app.competitors.CompetitorRepository import CompetitorRepository, ModalityRepository
from app.core.exceptions import NotFoundError


class CompetitorService:
    def __init__(self, db: Session):
        self.form_name = "Competitor"
        self.db = db
        self.repo = CompetitorRepository(CompetitorsEntity, db)
        self.repoModalities = ModalityRepository(ModalitiesEntity, db)

    def create_competitor(self, payload):
        session = self.db
        try:
            with session.begin():
                exist_competitor = self.repo.get_by_name_and_department(payload.competitor_name,
                                                                        payload.competitor_department)
                if not exist_competitor:
                    competitor = CompetitorsEntity(**payload.model_dump(exclude={"list_modalities"}))
                    competitor.competitor_id = uuid.uuid4()

                    competitor_created = self.repo.add(competitor)

                    for modality in payload.list_modalities:
                        modality_to_create = ModalitiesEntity(**modality.model_dump())
                        modality_to_create.modality_id = uuid.uuid4()
                        modality_to_create.competitor_id = competitor_created.competitor_id

                        self.repoModalities.add(modality_to_create)

                    return competitor_created.competitor_id
                else:
                    raise NotFoundError(f"{self.form_name} Error El usuario ya existe")
        except SQLAlchemyError as e:
            session.rollback()
            raise NotFoundError(f"{self.form_name} Error {e} not found.")

    def get_competitors(self, competitor_id):
        pass
