PGDMP  #    #                }            travel     13.20 (Debian 13.20-1.pgdg120+1)    17.0 |    n           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            o           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            p           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            q           1262    16384    travel    DATABASE     q   CREATE DATABASE travel WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';
    DROP DATABASE travel;
                     yourimagine    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                     yourimagine    false            r           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                        yourimagine    false    4            s           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                        yourimagine    false    4            �            1259    16416 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap r       yourimagine    false    4            �            1259    16414    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public               yourimagine    false    207    4            t           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public               yourimagine    false    206            �            1259    16426    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap r       yourimagine    false    4            �            1259    16424    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public               yourimagine    false    4    209            u           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public               yourimagine    false    208            �            1259    16408    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap r       yourimagine    false    4            �            1259    16406    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public               yourimagine    false    4    205            v           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public               yourimagine    false    204            �            1259    16460    core_country    TABLE     �  CREATE TABLE public.core_country (
    id bigint NOT NULL,
    country_name character varying(100) NOT NULL,
    country_code character varying(100) NOT NULL,
    currency_code character varying(100) NOT NULL,
    currency_name character varying(100) NOT NULL,
    visa_requirement character varying(50) NOT NULL,
    average_travel_cost numeric(10,2),
    description text NOT NULL,
    image_url text NOT NULL
);
     DROP TABLE public.core_country;
       public         heap r       yourimagine    false    4            �            1259    16458    core_country_id_seq    SEQUENCE     |   CREATE SEQUENCE public.core_country_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.core_country_id_seq;
       public               yourimagine    false    4    211            w           0    0    core_country_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.core_country_id_seq OWNED BY public.core_country.id;
          public               yourimagine    false    210            �            1259    16484    core_customuser    TABLE     �  CREATE TABLE public.core_customuser (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    budget numeric(10,2),
    currency character varying(10) NOT NULL,
    country_id bigint,
    country_code character varying(50),
    country character varying(50),
    currency_name character varying(50),
    currency_code character varying(50),
    average_travel_cost character varying(50),
    description character varying(50),
    image_url character varying(50),
    visa_requirement character varying(50)
);
 #   DROP TABLE public.core_customuser;
       public         heap r       yourimagine    false    4            �            1259    16497    core_customuser_groups    TABLE     �   CREATE TABLE public.core_customuser_groups (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    group_id integer NOT NULL
);
 *   DROP TABLE public.core_customuser_groups;
       public         heap r       yourimagine    false    4            �            1259    16495    core_customuser_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_customuser_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.core_customuser_groups_id_seq;
       public               yourimagine    false    4    217            x           0    0    core_customuser_groups_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.core_customuser_groups_id_seq OWNED BY public.core_customuser_groups.id;
          public               yourimagine    false    216            �            1259    16482    core_customuser_id_seq    SEQUENCE        CREATE SEQUENCE public.core_customuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.core_customuser_id_seq;
       public               yourimagine    false    4    215            y           0    0    core_customuser_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.core_customuser_id_seq OWNED BY public.core_customuser.id;
          public               yourimagine    false    214            �            1259    16505     core_customuser_user_permissions    TABLE     �   CREATE TABLE public.core_customuser_user_permissions (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    permission_id integer NOT NULL
);
 4   DROP TABLE public.core_customuser_user_permissions;
       public         heap r       yourimagine    false    4            �            1259    16503 '   core_customuser_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_customuser_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 >   DROP SEQUENCE public.core_customuser_user_permissions_id_seq;
       public               yourimagine    false    4    219            z           0    0 '   core_customuser_user_permissions_id_seq    SEQUENCE OWNED BY     s   ALTER SEQUENCE public.core_customuser_user_permissions_id_seq OWNED BY public.core_customuser_user_permissions.id;
          public               yourimagine    false    218            �            1259    16473    core_visarule    TABLE     A  CREATE TABLE public.core_visarule (
    id bigint NOT NULL,
    visa_requirement character varying(50) NOT NULL,
    visa_cost numeric(10,2),
    processing_time_days integer,
    additional_requirements text NOT NULL,
    max_stay_days integer,
    country_id bigint NOT NULL,
    passport_country_id bigint NOT NULL
);
 !   DROP TABLE public.core_visarule;
       public         heap r       yourimagine    false    4            �            1259    16471    core_visarule_id_seq    SEQUENCE     }   CREATE SEQUENCE public.core_visarule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.core_visarule_id_seq;
       public               yourimagine    false    213    4            {           0    0    core_visarule_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.core_visarule_id_seq OWNED BY public.core_visarule.id;
          public               yourimagine    false    212            �            1259    16561    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap r       yourimagine    false    4            �            1259    16559    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public               yourimagine    false    221    4            |           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public               yourimagine    false    220            �            1259    16398    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap r       yourimagine    false    4            �            1259    16396    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public               yourimagine    false    4    203            }           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public               yourimagine    false    202            �            1259    16387    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap r       yourimagine    false    4            �            1259    16385    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public               yourimagine    false    4    201            ~           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public               yourimagine    false    200            �            1259    16583    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap r       yourimagine    false    4            �           2604    16419    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public               yourimagine    false    207    206    207            �           2604    16429    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public               yourimagine    false    208    209    209            �           2604    16411    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public               yourimagine    false    204    205    205            �           2604    16463    core_country id    DEFAULT     r   ALTER TABLE ONLY public.core_country ALTER COLUMN id SET DEFAULT nextval('public.core_country_id_seq'::regclass);
 >   ALTER TABLE public.core_country ALTER COLUMN id DROP DEFAULT;
       public               yourimagine    false    211    210    211            �           2604    16487    core_customuser id    DEFAULT     x   ALTER TABLE ONLY public.core_customuser ALTER COLUMN id SET DEFAULT nextval('public.core_customuser_id_seq'::regclass);
 A   ALTER TABLE public.core_customuser ALTER COLUMN id DROP DEFAULT;
       public               yourimagine    false    215    214    215            �           2604    16500    core_customuser_groups id    DEFAULT     �   ALTER TABLE ONLY public.core_customuser_groups ALTER COLUMN id SET DEFAULT nextval('public.core_customuser_groups_id_seq'::regclass);
 H   ALTER TABLE public.core_customuser_groups ALTER COLUMN id DROP DEFAULT;
       public               yourimagine    false    217    216    217            �           2604    16508 #   core_customuser_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.core_customuser_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.core_customuser_user_permissions_id_seq'::regclass);
 R   ALTER TABLE public.core_customuser_user_permissions ALTER COLUMN id DROP DEFAULT;
       public               yourimagine    false    219    218    219            �           2604    16476    core_visarule id    DEFAULT     t   ALTER TABLE ONLY public.core_visarule ALTER COLUMN id SET DEFAULT nextval('public.core_visarule_id_seq'::regclass);
 ?   ALTER TABLE public.core_visarule ALTER COLUMN id DROP DEFAULT;
       public               yourimagine    false    212    213    213            �           2604    16564    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public               yourimagine    false    220    221    221            �           2604    16401    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public               yourimagine    false    202    203    203            �           2604    16390    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public               yourimagine    false    200    201    201            \          0    16416 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public               yourimagine    false    207   &�       ^          0    16426    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public               yourimagine    false    209   C�       Z          0    16408    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public               yourimagine    false    205   `�       `          0    16460    core_country 
   TABLE DATA           �   COPY public.core_country (id, country_name, country_code, currency_code, currency_name, visa_requirement, average_travel_cost, description, image_url) FROM stdin;
    public               yourimagine    false    211   ï       d          0    16484    core_customuser 
   TABLE DATA           -  COPY public.core_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, budget, currency, country_id, country_code, country, currency_name, currency_code, average_travel_cost, description, image_url, visa_requirement) FROM stdin;
    public               yourimagine    false    215   G�       f          0    16497    core_customuser_groups 
   TABLE DATA           M   COPY public.core_customuser_groups (id, customuser_id, group_id) FROM stdin;
    public               yourimagine    false    217   �       h          0    16505     core_customuser_user_permissions 
   TABLE DATA           \   COPY public.core_customuser_user_permissions (id, customuser_id, permission_id) FROM stdin;
    public               yourimagine    false    219   5�       b          0    16473    core_visarule 
   TABLE DATA           �   COPY public.core_visarule (id, visa_requirement, visa_cost, processing_time_days, additional_requirements, max_stay_days, country_id, passport_country_id) FROM stdin;
    public               yourimagine    false    213   R�       j          0    16561    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public               yourimagine    false    221   o�       X          0    16398    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public               yourimagine    false    203   ��       V          0    16387    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public               yourimagine    false    201   �       k          0    16583    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public               yourimagine    false    222   ��                  0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public               yourimagine    false    206            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public               yourimagine    false    208            �           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 32, true);
          public               yourimagine    false    204            �           0    0    core_country_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.core_country_id_seq', 1, false);
          public               yourimagine    false    210            �           0    0    core_customuser_groups_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.core_customuser_groups_id_seq', 1, false);
          public               yourimagine    false    216            �           0    0    core_customuser_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.core_customuser_id_seq', 1, true);
          public               yourimagine    false    214            �           0    0 '   core_customuser_user_permissions_id_seq    SEQUENCE SET     V   SELECT pg_catalog.setval('public.core_customuser_user_permissions_id_seq', 1, false);
          public               yourimagine    false    218            �           0    0    core_visarule_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.core_visarule_id_seq', 1, false);
          public               yourimagine    false    212            �           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);
          public               yourimagine    false    220            �           0    0    django_content_type_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.django_content_type_id_seq', 8, true);
          public               yourimagine    false    202            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 21, true);
          public               yourimagine    false    200            �           2606    16456    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public                 yourimagine    false    207            �           2606    16442 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public                 yourimagine    false    209    209            �           2606    16431 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public                 yourimagine    false    209            �           2606    16421    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public                 yourimagine    false    207            �           2606    16433 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public                 yourimagine    false    205    205            �           2606    16413 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public                 yourimagine    false    205            �           2606    16470 *   core_country core_country_country_name_key 
   CONSTRAINT     m   ALTER TABLE ONLY public.core_country
    ADD CONSTRAINT core_country_country_name_key UNIQUE (country_name);
 T   ALTER TABLE ONLY public.core_country DROP CONSTRAINT core_country_country_name_key;
       public                 yourimagine    false    211            �           2606    16468    core_country core_country_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.core_country
    ADD CONSTRAINT core_country_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.core_country DROP CONSTRAINT core_country_pkey;
       public                 yourimagine    false    211            �           2606    16532 R   core_customuser_groups core_customuser_groups_customuser_id_group_id_7990e9c6_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_groups
    ADD CONSTRAINT core_customuser_groups_customuser_id_group_id_7990e9c6_uniq UNIQUE (customuser_id, group_id);
 |   ALTER TABLE ONLY public.core_customuser_groups DROP CONSTRAINT core_customuser_groups_customuser_id_group_id_7990e9c6_uniq;
       public                 yourimagine    false    217    217            �           2606    16502 2   core_customuser_groups core_customuser_groups_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.core_customuser_groups
    ADD CONSTRAINT core_customuser_groups_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.core_customuser_groups DROP CONSTRAINT core_customuser_groups_pkey;
       public                 yourimagine    false    217            �           2606    16492 $   core_customuser core_customuser_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.core_customuser
    ADD CONSTRAINT core_customuser_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.core_customuser DROP CONSTRAINT core_customuser_pkey;
       public                 yourimagine    false    215            �           2606    16546 `   core_customuser_user_permissions core_customuser_user_per_customuser_id_permission_49ea742a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_user_permissions
    ADD CONSTRAINT core_customuser_user_per_customuser_id_permission_49ea742a_uniq UNIQUE (customuser_id, permission_id);
 �   ALTER TABLE ONLY public.core_customuser_user_permissions DROP CONSTRAINT core_customuser_user_per_customuser_id_permission_49ea742a_uniq;
       public                 yourimagine    false    219    219            �           2606    16510 F   core_customuser_user_permissions core_customuser_user_permissions_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_user_permissions
    ADD CONSTRAINT core_customuser_user_permissions_pkey PRIMARY KEY (id);
 p   ALTER TABLE ONLY public.core_customuser_user_permissions DROP CONSTRAINT core_customuser_user_permissions_pkey;
       public                 yourimagine    false    219            �           2606    16494 ,   core_customuser core_customuser_username_key 
   CONSTRAINT     k   ALTER TABLE ONLY public.core_customuser
    ADD CONSTRAINT core_customuser_username_key UNIQUE (username);
 V   ALTER TABLE ONLY public.core_customuser DROP CONSTRAINT core_customuser_username_key;
       public                 yourimagine    false    215            �           2606    16481     core_visarule core_visarule_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.core_visarule
    ADD CONSTRAINT core_visarule_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.core_visarule DROP CONSTRAINT core_visarule_pkey;
       public                 yourimagine    false    213            �           2606    16570 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public                 yourimagine    false    221            �           2606    16405 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public                 yourimagine    false    203    203            �           2606    16403 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public                 yourimagine    false    203            �           2606    16395 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public                 yourimagine    false    201            �           2606    16590 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public                 yourimagine    false    222            �           1259    16457    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public                 yourimagine    false    207            �           1259    16453 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public                 yourimagine    false    209            �           1259    16454 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public                 yourimagine    false    209            �           1259    16439 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public                 yourimagine    false    205            �           1259    16511 '   core_country_country_name_b99b6c31_like    INDEX     |   CREATE INDEX core_country_country_name_b99b6c31_like ON public.core_country USING btree (country_name varchar_pattern_ops);
 ;   DROP INDEX public.core_country_country_name_b99b6c31_like;
       public                 yourimagine    false    211            �           1259    16530 #   core_customuser_country_id_c3cc4fb9    INDEX     e   CREATE INDEX core_customuser_country_id_c3cc4fb9 ON public.core_customuser USING btree (country_id);
 7   DROP INDEX public.core_customuser_country_id_c3cc4fb9;
       public                 yourimagine    false    215            �           1259    16543 -   core_customuser_groups_customuser_id_976bc4d7    INDEX     y   CREATE INDEX core_customuser_groups_customuser_id_976bc4d7 ON public.core_customuser_groups USING btree (customuser_id);
 A   DROP INDEX public.core_customuser_groups_customuser_id_976bc4d7;
       public                 yourimagine    false    217            �           1259    16544 (   core_customuser_groups_group_id_301aeff4    INDEX     o   CREATE INDEX core_customuser_groups_group_id_301aeff4 ON public.core_customuser_groups USING btree (group_id);
 <   DROP INDEX public.core_customuser_groups_group_id_301aeff4;
       public                 yourimagine    false    217            �           1259    16557 7   core_customuser_user_permissions_customuser_id_ebd2ce6c    INDEX     �   CREATE INDEX core_customuser_user_permissions_customuser_id_ebd2ce6c ON public.core_customuser_user_permissions USING btree (customuser_id);
 K   DROP INDEX public.core_customuser_user_permissions_customuser_id_ebd2ce6c;
       public                 yourimagine    false    219            �           1259    16558 7   core_customuser_user_permissions_permission_id_80ceaab9    INDEX     �   CREATE INDEX core_customuser_user_permissions_permission_id_80ceaab9 ON public.core_customuser_user_permissions USING btree (permission_id);
 K   DROP INDEX public.core_customuser_user_permissions_permission_id_80ceaab9;
       public                 yourimagine    false    219            �           1259    16529 &   core_customuser_username_0e60666f_like    INDEX     z   CREATE INDEX core_customuser_username_0e60666f_like ON public.core_customuser USING btree (username varchar_pattern_ops);
 :   DROP INDEX public.core_customuser_username_0e60666f_like;
       public                 yourimagine    false    215            �           1259    16522 !   core_visarule_country_id_996bdb59    INDEX     a   CREATE INDEX core_visarule_country_id_996bdb59 ON public.core_visarule USING btree (country_id);
 5   DROP INDEX public.core_visarule_country_id_996bdb59;
       public                 yourimagine    false    213            �           1259    16523 *   core_visarule_passport_country_id_b79dfd01    INDEX     s   CREATE INDEX core_visarule_passport_country_id_b79dfd01 ON public.core_visarule USING btree (passport_country_id);
 >   DROP INDEX public.core_visarule_passport_country_id_b79dfd01;
       public                 yourimagine    false    213            �           1259    16581 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public                 yourimagine    false    221            �           1259    16582 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public                 yourimagine    false    221            �           1259    16592 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public                 yourimagine    false    222            �           1259    16591 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public                 yourimagine    false    222            �           2606    16448 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public               yourimagine    false    209    205    2968            �           2606    16443 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public               yourimagine    false    207    2973    209            �           2606    16434 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public               yourimagine    false    2963    205    203            �           2606    16524 F   core_customuser core_customuser_country_id_c3cc4fb9_fk_core_country_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser
    ADD CONSTRAINT core_customuser_country_id_c3cc4fb9_fk_core_country_id FOREIGN KEY (country_id) REFERENCES public.core_country(id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.core_customuser DROP CONSTRAINT core_customuser_country_id_c3cc4fb9_fk_core_country_id;
       public               yourimagine    false    215    2984    211            �           2606    16533 O   core_customuser_groups core_customuser_grou_customuser_id_976bc4d7_fk_core_cust    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_groups
    ADD CONSTRAINT core_customuser_grou_customuser_id_976bc4d7_fk_core_cust FOREIGN KEY (customuser_id) REFERENCES public.core_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.core_customuser_groups DROP CONSTRAINT core_customuser_grou_customuser_id_976bc4d7_fk_core_cust;
       public               yourimagine    false    217    215    2991            �           2606    16538 P   core_customuser_groups core_customuser_groups_group_id_301aeff4_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_groups
    ADD CONSTRAINT core_customuser_groups_group_id_301aeff4_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.core_customuser_groups DROP CONSTRAINT core_customuser_groups_group_id_301aeff4_fk_auth_group_id;
       public               yourimagine    false    217    2973    207            �           2606    16547 Y   core_customuser_user_permissions core_customuser_user_customuser_id_ebd2ce6c_fk_core_cust    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_user_permissions
    ADD CONSTRAINT core_customuser_user_customuser_id_ebd2ce6c_fk_core_cust FOREIGN KEY (customuser_id) REFERENCES public.core_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_customuser_user_permissions DROP CONSTRAINT core_customuser_user_customuser_id_ebd2ce6c_fk_core_cust;
       public               yourimagine    false    215    2991    219            �           2606    16552 Y   core_customuser_user_permissions core_customuser_user_permission_id_80ceaab9_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_user_permissions
    ADD CONSTRAINT core_customuser_user_permission_id_80ceaab9_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_customuser_user_permissions DROP CONSTRAINT core_customuser_user_permission_id_80ceaab9_fk_auth_perm;
       public               yourimagine    false    219    205    2968            �           2606    16512 B   core_visarule core_visarule_country_id_996bdb59_fk_core_country_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_visarule
    ADD CONSTRAINT core_visarule_country_id_996bdb59_fk_core_country_id FOREIGN KEY (country_id) REFERENCES public.core_country(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.core_visarule DROP CONSTRAINT core_visarule_country_id_996bdb59_fk_core_country_id;
       public               yourimagine    false    213    211    2984            �           2606    16517 K   core_visarule core_visarule_passport_country_id_b79dfd01_fk_core_country_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_visarule
    ADD CONSTRAINT core_visarule_passport_country_id_b79dfd01_fk_core_country_id FOREIGN KEY (passport_country_id) REFERENCES public.core_country(id) DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.core_visarule DROP CONSTRAINT core_visarule_passport_country_id_b79dfd01_fk_core_country_id;
       public               yourimagine    false    213    211    2984            �           2606    16571 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public               yourimagine    false    221    203    2963            �           2606    16576 H   django_admin_log django_admin_log_user_id_c564eba6_fk_core_customuser_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_core_customuser_id FOREIGN KEY (user_id) REFERENCES public.core_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_core_customuser_id;
       public               yourimagine    false    221    215    2991            \      x������ � �      ^      x������ � �      Z   S  x�]�K��0��ur
N0j³�F�*�D騷p��fG̷�e%F}�S�v]6�}�}�(����q���@����;�`�s��%#�����;��T���5l�0O�Bt���:fk�',2�P�����=U����C |ks�q�?v!1�)�Ab)%���y*x��~�.�?�S���hS��*�K�v�(|E���֩zsa�%�I��ǒ����Efo�F�1l�nd�+��X��h���rk���!+��"�=!���6[��TM��<j+�?g�ER�~.��$���A)��~s�j²��ϯs�sq���e1&^ ��,��+@�E����      `      x��Z�v�H��_}��4��.� !��IN�I(	�����<e��gN����ԟ���} q��m<�x���7=w*"O�"�� ���?����O&����PP|����+��%�Cbu_Te�6�r�W{��\��-�3�2�g�Zu�C�+%�%�)��j���n�ύI`�[����{/�7���~>��?m;�ʛ��wt���S�̈́��K(+s02u8rLB��#��@�Du_���0���o�}��%�B� ҩ�u-�*l�z��,0YssLX�n�2Ym�r�2A�N�x�+f�m����Uy��^�a�Y�S1����T��Y�K	B���n���^���m�?$KLE(��s:�Țj��<+��1�^F���\�G6ѻ_�zJ�6'�4��*�wE���XNYdY<6y�y:YrL� D0Xr*н{z����ͪh���Y]/�=����z�,ɂ9c��{q��i�+���}�'dO�1����a�R�-[*d���ĳU���3���)c�҆���j[�Z1!�8�f�0~N�L��R/�D`�oSiē� ��6��+���	b������Ԑ��zl�Z��,�_uG��5�f�J��n<c÷<�L�do�_�j[B�0���s��`�9SB�nժ�9��L����tk�R�m�o�=ȯ6�Vi}\��pB[�����U��Z6\y����9�MuDF*����~�8}�m�P��"�ے^�R��ڭ��d <#\��f�0:���}^�����A}��!7c"tL�D�c7�K�����7��X��l�[�+��3�Iv2#{�6�����+�t��k��?wh����H�E+��wK�١�O�hwR�-c���M�9Xq�����D�"�����^`��z~��i���N�y�'����&k(�dV���,���[�=��R�񷙆`�l�L([�w���M6���Vp�Kf��S�o��Ů���c��iS� ��*$Q�{��?�w�� ����%bN�~8���;�:��8��R� %p����Y�����X���1�B2��M�9��!d#�֜�#��V��≱����$��ͪx*������ۺBq쟾>�D��f,�䰓�����`![y �y��*o!�F�@�У��*��j��߭ۀ4�9����gĶ���3%��_8��͹����E՘�@�Zq�����]�nu�Y$��М�5P�R��3#G��>�ߋ���T/�AK���_�,Fh'ۛ�RFrd
���|���Q�ɹ��S��&��V�lv���3��^�rw��Z�ˎ�̕�J����j�X�芤��Pܾ�Gc��"I�	�tlk� f���I$K���t0#=�I�����������$�1����H
r��o��e�P�
|hA����_��t@R�1��hO-�rH2�zq���d��>��/�VY�/{9�q�Y-�P@���l�4�Ͼt�R�� b���>M��&��s�Zm$>��fR�<�̉��2��1M<�Τ&�&�o'9��Q!ў�����EdKn�:M�WF�h�+7����[�$��i�@�HXqɑ_Z^�Gu�R*x�}Y���1$�7���q5B?��Dnh�Hm�?����\+�D����W��B]���11t�ir�r�.����r=�LA*�%�7�&ۼ:R��G���wDOV�ug�5�������\��H�A��A�%X78���!3�x���#�O%�+�`L?��]���Մc8�f�\���Z(D���E�.��-#d��s��M!|]�G3��by�3�Y����-S�ڨ{��3+��\�h*P�Ҵ&���\�ݧ����o��;�)���0�ŀ�p	CK��ș8ǆCpE��������/e��������M}&�
@���d�K�fJ���	M�v���<[֖�W���uHb�zYuLuQ�O�"o}׀�/E') ntǍ�{NB��C}�Xz�!�?������ q�S��jp�*;K��c�G<@����x#7/���e��2\3�����������e������*$5�C�{�y��<_�����9Y��k�u��׹�XY@��"�ή&ԺEw� �}-�ѵ|Ǎz �ױrx$�k�כꮑ摬��}���>z�O������S'��/���'H�_��>xyTY�k����g�������#O�U����@������6�p����n�:�ټ�z��p£��?�jN��#�9���9��2�[^nO,ɼLR�b�Hǅt\Mz��">��k�z��`�-�/��1����&(��L�=������)A���\�f��| u�N��fB��lˮ�O�g�烁�(@Rʛ����Հ9̷�`Q�=���v�RNe�S�0�� �&���OOG���x�4�.��,{� ���&Δ�?�9�(6d�'��Q�|��v	��᪮��$V���"sc�ٱ-���LNq�F��!ҥ+��:.���%�}��lH�z�{ęn�QX����݆�����/\h���znN��0�ew���x3�U��(�q���|�_�0V��� �C.1���Y��JOE�T�!��kI�č!)���LR��~6)+&C�V+7T)(�xw���;����
kbq�*����8oY�8M����%�����17~�(,�v�Uz���'��>���Hx�t�3:]��s��rN<{-��(�B'�p���|���v�@H� �t����1��H�a�������%s�����>���W5�Fi��!D2�Qa�B���m�۵��o��m�r������:��\'�ʎ�.!������}Wa����L$���g���/G����:��9�a��MyZrG���"л��8��(J���>�82!`�H2�8��(8���Grn�"hBEv�*<��2�R�������"=`a��J�*�_��l���Mn�/[ �< �v�R��ߗ�����21�=��#����H�b5��������g\= gi�Y���8�#Q�KUc�\,�y�t�Ts=�L|.�������H���$�J|�d�|ڞV��̰ �$����1sH� ')ѐ�#:� 2�0�l܀,������^��?�Ll{В���S�K�,�4ư@Z Y����� �	��Co:�M�^�%	�iE� t'S�C�a�/��^@���ڂ��Ď~`����lh ����ͶKz��	 s၉:��@�	 ^�1`�u�����E2�ʣ
 X����`E��p�bK�'�8�m��Զ!0���b�0�^t|�2���n�@{��р&��A`��T�_�XȒ�?��pAV�ow�g�� ��U*'�C�T�m8°�h*HO#PB:>3��
��q�4���{i��Er�0�~|
��nF��E������4%���t�����	�݌H<d,٠e�.ԥ�31�@�̀��C#���,��fv�ý�&5��sd���������ע�aQLa�lp�F�ͦaʑ�%�t
��9���e>����x8�;>��0k���ت�;�6�5�wx�~��hi��N�F�G��nN��	� hì�H/l�6V.�o�R�QH4��5�B�DqD@� >Vx�y&����^���u��.Gɚ�:40�nlV aN�v6�?���	L�]>���?��������W�@���`���i�竘�W\&н���6-�wy����	l_O���h	�_B�*����ox����	7���9s��,���X��j?���k־�"6;�^��;�f�M��_��;ӄJ�g`E�^�!7�ן�c1�Q^u%����^_Մ��;�P������_珧�Pߌ�^Qͩ�u�8���)	Lz��3�%=_�F����}��a���#�G��%| ��=�\�_Ͻt�Ԇ ������#yA��pj�� �E<W��&�z*�9.Qq��t����@�<5�7��og�=�޾�I�}Pm������������KF4�ҥ o   i���&�Zp�O�T4��W4ۮ@�����$��# ���S
zﳋ�|�EX���d6��`�Oc���_Ps���!SF�#Jc��?JS&�쮾9�S����%ƔBn���R�Rح˧��:�23��7X���������Ws�wE�����0�y�㢺&�>������&g�4���:��b@}�(���j��0h@�(���S�)��!�-ebJ���+̧����jo���j���A���P���v��|��!�2�@��'^S�t�b^�^�X���Msp�ν��!r�24�;h�^�����4�����v�~C���}��X������7���|Ȁ$��w���3�xL�y��--�w|����{P�_�=h&�L�Ͳ4�Y��u�CB~�KX�~��R�ӎ�0��4_'�ψf�L볈�A��"��%���>#��)]�!]��~ѿ|���1bLs^��~�*.x���]М#����/*���Csԣ�����hQ��bsdR}�Z�9-��K��C>sԧ�Z�B�Y�в|��o���I�����k`�{��4=ʣ���sD�+�<��_~���ק�      d   �   x�m�I�P���_��]d������* _��8����U���>�̿�1��G�P9�o�x������5͟�nUK�5Q��:��w٣2qo�����dꄞ-��$]�AwV�@�D���Z���G�4D�1��*� �HVE�o�9�f� �}��g�-�YH�@�O�ό�pX��� ���*MQ���=D      f      x������ � �      h      x������ � �      b      x������ � �      j      x������ � �      X   k   x�MLI
�0<kSh��1��T���2Z�}M�B/��gJ��+-2su�p����Z�Y���pf�h��$�{շ��/p#�}a?�{/(w���q�5[�X�o�R�X1� | �i2�      V   �  x����n� ������U#��,+!�P�6.�y�qI�ƛH���1�p������y��C�v�K�F�� ���SB�T*��/B;���`G�a���ˎ��h� E:���Ǉ3"+�`m�d��m]��O�@=�O=ة�_�%Q�YE��"+j�y��q�c
gL
ozK)Km��)�G0$IE��`���Ĥ߻,l6|a��z)�Ax���Ņv��t�l�!����k#fp'�|�ڜNچ��m����8� P�ɻ�<�KP�/�FR�z
%�����7
Њ�_�'1���@�-�^���s��4n�#A�}hQ|+�ՅgUIN�E�#��9�!Q�9���MO�pB�E������p����Ɨ�l@�e�@^��(�2�T��u0�>�yw܈\��U���cRHR��Q��!Yj��G�8�Þ``��Rh������{P�����n����`      k   7  x�=�G��X  �u�)z?r����&g[#!�ɘ���]���
O�C^w#�akG�FA2MD�tS쿾��5��.?���qm�![(50����Es���]]S�Q�G�˳�4w��q����ׁ���5�M}�é<����9�ǘ;:�O,2��/�K�y����x�@�f�\�oӷG�u��QV$~>S����~����,�+��IT�au�BބJ�4_w�`κ�'U���/�A��'H���3	�Y���?��d	���u�$Y�V�]��cbSv#�#j�u��V�A}�o`��Ѻ\�����R��E0��U�&Nc�ܝv,�<cE�+Ah��f�΋'<j�l��S��B7S҂�ˬݦEU'�OC��������Z��/J(	�8[u��y�[ovZ�����w��Z�T�>��:9��*��k�(�-�Y�z�e��$���
�I���%����Or�Bk����P�<�P�_�ur���H���w�#JY��/�#I�}=��z�����y��zݏ-�.�a#Dv�� �(��M~���O�S�I�ܮ;1��G�4y��h8��vo���%\���o%C�������߇�<�$#~R�CL���v/�6�5��U��1sڦ�jb�P�$��;4������ �o�}Sp*����>�]�n*+&��^Y�$?f |�E��Xڮ��
U#�u�&�]�Ɓ8I��mTF� �M��d���b�Ԧ�d1�tfߙ����fg&����qiba��(��;B;��9��^\����?v���8�v�g�� �,�;��ﯯ�?�V     