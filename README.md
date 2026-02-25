Проект интернет-магазина

    catalog(request):
    """контроллер для страницы home.html"""
    

    catalog_con(request):
    """контроллер для страницы contacts.html"""
    
20260225
Задание 1
Подключите СУБД PostgreSQL для работы в проекте.

CREATE TABLE IF NOT EXISTS public.product
(
    p_idd integer NOT NULL,
    p_name character varying COLLATE pg_catalog."default",
    p_descr character varying COLLATE pg_catalog."default",
    p_image character varying COLLATE pg_catalog."default",
    p_category integer,
    p_cost double precision,
    p_create date,
    p_change date,
    CONSTRAINT "PK_product" PRIMARY KEY (p_idd),
    CONSTRAINT fk_category FOREIGN KEY (p_category)
        REFERENCES public.category (c_idd) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.product
    OWNER to postgres;

CREATE TABLE IF NOT EXISTS public.category
(
    c_idd integer NOT NULL,
    c_name character varying COLLATE pg_catalog."default",
    c_descr character varying COLLATE pg_catalog."default",
    CONSTRAINT "PK_category" PRIMARY KEY (c_idd)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.category
    OWNER to postgres;
