CREATE TABLE IF NOT EXISTS public.questions
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    data character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT questions_pkey PRIMARY KEY (id)
)

    TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.questions
    OWNER to postgres;


CREATE TABLE IF NOT EXISTS public.answers
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    data character varying COLLATE pg_catalog."default" NOT NULL,
    question_id integer NOT NULL,
    quality character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT answers_pkey PRIMARY KEY (id),
    CONSTRAINT answers_question_id_fkey FOREIGN KEY (question_id)
        REFERENCES public.questions (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

    TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.answers
    OWNER to postgres;



DROP TABLE IF EXISTS public.answers;
DROP TABLE IF EXISTS public.questions;
