create table competitors
(
    competitor_id             uuid not null primary key,
    type_competence           varchar,
    department                varchar,
    city                      varchar,
    competitor_name           varchar,
    competitor_gender         varchar,
    competitor_category       varchar,
    competitor_birthdate      date,
    modality                  varchar,
    first_attempt             int,
    second_attempt            int,
    third_attempt             int,
    total_olympic             int,
    state                     varchar,
    created_at                timestamp,
    updated_at                timestamp,
    deleted_at                timestamp,
    created_by                uuid,
    updated_by                uuid,
    deleted_by                uuid,
    status                    smallint default 1
);