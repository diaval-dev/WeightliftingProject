create table competitors
(
    competitor_id             uuid not null primary key,
    type_competence           varchar,
    competitor_name           varchar,
    competitor_gender         varchar,
    competitor_category       varchar,
    competitor_birthdate      date,
    competitor_university     varchar,
    competitor_department     varchar,
    total_olympic             int,
    created_at                timestamp,
    updated_at                timestamp,
    deleted_at                timestamp,
    created_by                uuid,
    updated_by                uuid,
    deleted_by                uuid,
    status                    smallint default 1
);


create table modalities
(
    modality_id               uuid not null primary key,
    competitor_id             uuid,
    modality_name             varchar,
    first_attempt             int,
    state_first_attempt       varchar,
    second_attempt            int,
    state_second_attempt      varchar,
    third_attempt             int,
    state_third_attempt       varchar,
    total                     int,
    created_at                timestamp,
    updated_at                timestamp,
    deleted_at                timestamp,
    created_by                uuid,
    updated_by                uuid,
    deleted_by                uuid,
    status                    smallint default 1
)