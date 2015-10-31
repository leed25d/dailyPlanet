--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: groups; Type: TABLE; Schema: public; Owner: lee; Tablespace: 
--

CREATE TABLE groups (
    id integer NOT NULL,
    name character varying(40) NOT NULL
);


ALTER TABLE public.groups OWNER TO lee;

--
-- Name: groups_id_seq; Type: SEQUENCE; Schema: public; Owner: lee
--

CREATE SEQUENCE groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.groups_id_seq OWNER TO lee;

--
-- Name: groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lee
--

ALTER SEQUENCE groups_id_seq OWNED BY groups.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: lee; Tablespace: 
--

CREATE TABLE users (
    id integer NOT NULL,
    first_name character varying(40) NOT NULL,
    last_name character varying(40) NOT NULL,
    userid character varying(40) NOT NULL
);


ALTER TABLE public.users OWNER TO lee;

--
-- Name: users_groups; Type: TABLE; Schema: public; Owner: lee; Tablespace: 
--

CREATE TABLE users_groups (
    users_id integer,
    groups_id integer
);


ALTER TABLE public.users_groups OWNER TO lee;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: lee
--

CREATE SEQUENCE users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO lee;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: lee
--

ALTER SEQUENCE users_id_seq OWNED BY users.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: lee
--

ALTER TABLE ONLY groups ALTER COLUMN id SET DEFAULT nextval('groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: lee
--

ALTER TABLE ONLY users ALTER COLUMN id SET DEFAULT nextval('users_id_seq'::regclass);


--
-- Data for Name: groups; Type: TABLE DATA; Schema: public; Owner: lee
--

COPY groups (id, name) FROM stdin;
1	group1
2	group2
3	group3
\.


--
-- Name: groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: lee
--

SELECT pg_catalog.setval('groups_id_seq', 3, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: lee
--

COPY users (id, first_name, last_name, userid) FROM stdin;
1	Joe	Smith	jsmith
2	John	Doe	jdoe
\.


--
-- Data for Name: users_groups; Type: TABLE DATA; Schema: public; Owner: lee
--

COPY users_groups (users_id, groups_id) FROM stdin;
1	1
2	2
1	3
2	3
\.


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: lee
--

SELECT pg_catalog.setval('users_id_seq', 2, true);


--
-- Name: groups_pkey; Type: CONSTRAINT; Schema: public; Owner: lee; Tablespace: 
--

ALTER TABLE ONLY groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: lee; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users_groups_groups_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lee
--

ALTER TABLE ONLY users_groups
    ADD CONSTRAINT users_groups_groups_id_fkey FOREIGN KEY (groups_id) REFERENCES groups(id) ON UPDATE CASCADE;


--
-- Name: users_groups_users_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: lee
--

ALTER TABLE ONLY users_groups
    ADD CONSTRAINT users_groups_users_id_fkey FOREIGN KEY (users_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

