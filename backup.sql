--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: noda; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.noda (
    userid character varying(127) NOT NULL,
    password character varying(255) NOT NULL
);


ALTER TABLE public.noda OWNER TO postgres;

--
-- Name: nodadate; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.nodadate (
    userid character varying(127) NOT NULL,
    hinichi date,
    content character varying(2048) NOT NULL
);


ALTER TABLE public.nodadate OWNER TO postgres;

--
-- Name: nodaschedule; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.nodaschedule (
    userid character varying(127) NOT NULL,
    starttime timestamp without time zone,
    endtime timestamp without time zone,
    content character varying(2048) NOT NULL
);


ALTER TABLE public.nodaschedule OWNER TO postgres;

--
-- Data for Name: noda; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.noda (userid, password) FROM stdin;
\.


--
-- Data for Name: nodadate; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.nodadate (userid, hinichi, content) FROM stdin;
\.


--
-- Data for Name: nodaschedule; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.nodaschedule (userid, starttime, endtime, content) FROM stdin;
\.


--
-- PostgreSQL database dump complete
--

