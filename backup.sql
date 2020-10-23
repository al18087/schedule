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
-- Name: mybook; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user (
    userid character varying(127) NOT NULL,
    password character varying(255) NOT NULL
);


ALTER TABLE public.user OWNER TO postgres;

--
-- Name: scheduledate; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.schedule (
    userid character varying(127) NOT NULL,
    hinichi date,
    content character varying(2048) NOT NULL
);


ALTER TABLE public.schedule OWNER TO postgres;

--
-- Name: yotei; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scheduleyotei (
    userid character varying(127) NOT NULL,
    starttime timestamp without time zone,
    endtime timestamp without time zone,
    content character varying(2048) NOT NULL
);


ALTER TABLE public.scheduleyotei OWNER TO postgres;

--
-- Data for Name: mybook; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user (userid, password) FROM stdin;
\.


--
-- Data for Name: scheduledate; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.schedule (userid, hinichi, content) FROM stdin;
\.


--
-- Data for Name: yotei; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.scheduleyotei (userid, starttime, endtime, content) FROM stdin;
\.


--
-- Name: TABLE mybook; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE ON TABLE public.user TO calendaruser;


--
-- Name: TABLE scheduledate; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE ON TABLE public.schedule TO calendaruser;


--
-- Name: TABLE yotei; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT,DELETE ON TABLE public.scheduleyotei TO calendaruser;


--
-- PostgreSQL database dump complete
--

