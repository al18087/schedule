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
-- Name: info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.info (
    userid character varying(127) NOT NULL,
    password character varying(255) NOT NULL
);


ALTER TABLE public.info OWNER TO postgres;

--
-- Name: schedule; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.schedule (
    userid character varying(127) NOT NULL,
    starttime timestamp without time zone,
    endtime timestamp without time zone,
    content character varying(2048) NOT NULL
);


ALTER TABLE public.schedule OWNER TO postgres;

--
-- Name: scheduledate; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scheduledate (
    userid character varying(127) NOT NULL,
    hinichi date,
    content character varying(2048) NOT NULL
);


ALTER TABLE public.scheduledate OWNER TO postgres;

--
-- Data for Name: info; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.info (userid, password) FROM stdin;
\.


--
-- Data for Name: schedule; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.schedule (userid, starttime, endtime, content) FROM stdin;
\.


--
-- Data for Name: scheduledate; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.scheduledate (userid, hinichi, content) FROM stdin;
\.


--
-- PostgreSQL database dump complete
--

