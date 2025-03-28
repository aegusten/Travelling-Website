PGDMP                          }            travel     13.20 (Debian 13.20-1.pgdg120+1)     13.20 (Debian 13.20-1.pgdg120+1) y    n           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            o           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            p           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            q           1262    16384    travel    DATABASE     Z   CREATE DATABASE travel WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';
    DROP DATABASE travel;
                yourimagine    false            �            1259    16416 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    yourimagine    false            �            1259    16414    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          yourimagine    false    207            r           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          yourimagine    false    206            �            1259    16426    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    yourimagine    false            �            1259    16424    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          yourimagine    false    209            s           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          yourimagine    false    208            �            1259    16408    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    yourimagine    false            �            1259    16406    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          yourimagine    false    205            t           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          yourimagine    false    204            �            1259    16460    core_country    TABLE     �  CREATE TABLE public.core_country (
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
       public         heap    yourimagine    false            �            1259    16458    core_country_id_seq    SEQUENCE     |   CREATE SEQUENCE public.core_country_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.core_country_id_seq;
       public          yourimagine    false    211            u           0    0    core_country_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.core_country_id_seq OWNED BY public.core_country.id;
          public          yourimagine    false    210            �            1259    16484    core_customuser    TABLE     B  CREATE TABLE public.core_customuser (
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
    country_id bigint
);
 #   DROP TABLE public.core_customuser;
       public         heap    yourimagine    false            �            1259    16497    core_customuser_groups    TABLE     �   CREATE TABLE public.core_customuser_groups (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    group_id integer NOT NULL
);
 *   DROP TABLE public.core_customuser_groups;
       public         heap    yourimagine    false            �            1259    16495    core_customuser_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_customuser_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.core_customuser_groups_id_seq;
       public          yourimagine    false    215            v           0    0    core_customuser_groups_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.core_customuser_groups_id_seq OWNED BY public.core_customuser_groups.id;
          public          yourimagine    false    214            �            1259    16482    core_customuser_id_seq    SEQUENCE        CREATE SEQUENCE public.core_customuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.core_customuser_id_seq;
       public          yourimagine    false    213            w           0    0    core_customuser_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.core_customuser_id_seq OWNED BY public.core_customuser.id;
          public          yourimagine    false    212            �            1259    16505     core_customuser_user_permissions    TABLE     �   CREATE TABLE public.core_customuser_user_permissions (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    permission_id integer NOT NULL
);
 4   DROP TABLE public.core_customuser_user_permissions;
       public         heap    yourimagine    false            �            1259    16503 '   core_customuser_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.core_customuser_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 >   DROP SEQUENCE public.core_customuser_user_permissions_id_seq;
       public          yourimagine    false    217            x           0    0 '   core_customuser_user_permissions_id_seq    SEQUENCE OWNED BY     s   ALTER SEQUENCE public.core_customuser_user_permissions_id_seq OWNED BY public.core_customuser_user_permissions.id;
          public          yourimagine    false    216            �            1259    16595    core_visarule    TABLE     A  CREATE TABLE public.core_visarule (
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
       public         heap    yourimagine    false            �            1259    16601    core_visarule_id_seq    SEQUENCE     }   CREATE SEQUENCE public.core_visarule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.core_visarule_id_seq;
       public          yourimagine    false    221            y           0    0    core_visarule_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.core_visarule_id_seq OWNED BY public.core_visarule.id;
          public          yourimagine    false    222            �            1259    16561    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
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
       public         heap    yourimagine    false            �            1259    16559    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          yourimagine    false    219            z           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          yourimagine    false    218            �            1259    16398    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    yourimagine    false            �            1259    16396    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          yourimagine    false    203            {           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          yourimagine    false    202            �            1259    16387    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    yourimagine    false            �            1259    16385    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          yourimagine    false    201            |           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          yourimagine    false    200            �            1259    16584    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    yourimagine    false            �           2604    16628    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          yourimagine    false    207    206    207            �           2604    16629    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          yourimagine    false    209    208    209            �           2604    16630    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          yourimagine    false    205    204    205            �           2604    16631    core_country id    DEFAULT     r   ALTER TABLE ONLY public.core_country ALTER COLUMN id SET DEFAULT nextval('public.core_country_id_seq'::regclass);
 >   ALTER TABLE public.core_country ALTER COLUMN id DROP DEFAULT;
       public          yourimagine    false    211    210    211            �           2604    16632    core_customuser id    DEFAULT     x   ALTER TABLE ONLY public.core_customuser ALTER COLUMN id SET DEFAULT nextval('public.core_customuser_id_seq'::regclass);
 A   ALTER TABLE public.core_customuser ALTER COLUMN id DROP DEFAULT;
       public          yourimagine    false    213    212    213            �           2604    16633    core_customuser_groups id    DEFAULT     �   ALTER TABLE ONLY public.core_customuser_groups ALTER COLUMN id SET DEFAULT nextval('public.core_customuser_groups_id_seq'::regclass);
 H   ALTER TABLE public.core_customuser_groups ALTER COLUMN id DROP DEFAULT;
       public          yourimagine    false    215    214    215            �           2604    16634 #   core_customuser_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.core_customuser_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.core_customuser_user_permissions_id_seq'::regclass);
 R   ALTER TABLE public.core_customuser_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          yourimagine    false    217    216    217            �           2604    16635    core_visarule id    DEFAULT     t   ALTER TABLE ONLY public.core_visarule ALTER COLUMN id SET DEFAULT nextval('public.core_visarule_id_seq'::regclass);
 ?   ALTER TABLE public.core_visarule ALTER COLUMN id DROP DEFAULT;
       public          yourimagine    false    222    221            �           2604    16636    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          yourimagine    false    218    219    219            �           2604    16637    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          yourimagine    false    202    203    203            �           2604    16638    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          yourimagine    false    200    201    201            \          0    16416 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          yourimagine    false    207   E�       ^          0    16426    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          yourimagine    false    209   b�       Z          0    16408    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          yourimagine    false    205   �       `          0    16460    core_country 
   TABLE DATA           �   COPY public.core_country (id, country_name, country_code, currency_code, currency_name, visa_requirement, average_travel_cost, description, image_url) FROM stdin;
    public          yourimagine    false    211   ��       b          0    16484    core_customuser 
   TABLE DATA           �   COPY public.core_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, budget, currency, country_id) FROM stdin;
    public          yourimagine    false    213   B�       d          0    16497    core_customuser_groups 
   TABLE DATA           M   COPY public.core_customuser_groups (id, customuser_id, group_id) FROM stdin;
    public          yourimagine    false    215   �       f          0    16505     core_customuser_user_permissions 
   TABLE DATA           \   COPY public.core_customuser_user_permissions (id, customuser_id, permission_id) FROM stdin;
    public          yourimagine    false    217   �       j          0    16595    core_visarule 
   TABLE DATA           �   COPY public.core_visarule (id, visa_requirement, visa_cost, processing_time_days, additional_requirements, max_stay_days, country_id, passport_country_id) FROM stdin;
    public          yourimagine    false    221   ;�       h          0    16561    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          yourimagine    false    219   X�       X          0    16398    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          yourimagine    false    203   u�       V          0    16387    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          yourimagine    false    201   �       i          0    16584    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          yourimagine    false    220   վ       }           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          yourimagine    false    206            ~           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          yourimagine    false    208                       0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 32, true);
          public          yourimagine    false    204            �           0    0    core_country_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.core_country_id_seq', 1, false);
          public          yourimagine    false    210            �           0    0    core_customuser_groups_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.core_customuser_groups_id_seq', 1, false);
          public          yourimagine    false    214            �           0    0    core_customuser_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.core_customuser_id_seq', 2, true);
          public          yourimagine    false    212            �           0    0 '   core_customuser_user_permissions_id_seq    SEQUENCE SET     V   SELECT pg_catalog.setval('public.core_customuser_user_permissions_id_seq', 1, false);
          public          yourimagine    false    216            �           0    0    core_visarule_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.core_visarule_id_seq', 1, false);
          public          yourimagine    false    222            �           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);
          public          yourimagine    false    218            �           0    0    django_content_type_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.django_content_type_id_seq', 8, true);
          public          yourimagine    false    202            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 21, true);
          public          yourimagine    false    200            �           2606    16456    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            yourimagine    false    207            �           2606    16442 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            yourimagine    false    209    209            �           2606    16431 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            yourimagine    false    209            �           2606    16421    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            yourimagine    false    207            �           2606    16433 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            yourimagine    false    205    205            �           2606    16413 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            yourimagine    false    205            �           2606    16470 *   core_country core_country_country_name_key 
   CONSTRAINT     m   ALTER TABLE ONLY public.core_country
    ADD CONSTRAINT core_country_country_name_key UNIQUE (country_name);
 T   ALTER TABLE ONLY public.core_country DROP CONSTRAINT core_country_country_name_key;
       public            yourimagine    false    211            �           2606    16468    core_country core_country_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.core_country
    ADD CONSTRAINT core_country_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.core_country DROP CONSTRAINT core_country_pkey;
       public            yourimagine    false    211            �           2606    16532 R   core_customuser_groups core_customuser_groups_customuser_id_group_id_7990e9c6_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_groups
    ADD CONSTRAINT core_customuser_groups_customuser_id_group_id_7990e9c6_uniq UNIQUE (customuser_id, group_id);
 |   ALTER TABLE ONLY public.core_customuser_groups DROP CONSTRAINT core_customuser_groups_customuser_id_group_id_7990e9c6_uniq;
       public            yourimagine    false    215    215            �           2606    16502 2   core_customuser_groups core_customuser_groups_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.core_customuser_groups
    ADD CONSTRAINT core_customuser_groups_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.core_customuser_groups DROP CONSTRAINT core_customuser_groups_pkey;
       public            yourimagine    false    215            �           2606    16492 $   core_customuser core_customuser_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.core_customuser
    ADD CONSTRAINT core_customuser_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.core_customuser DROP CONSTRAINT core_customuser_pkey;
       public            yourimagine    false    213            �           2606    16546 `   core_customuser_user_permissions core_customuser_user_per_customuser_id_permission_49ea742a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_user_permissions
    ADD CONSTRAINT core_customuser_user_per_customuser_id_permission_49ea742a_uniq UNIQUE (customuser_id, permission_id);
 �   ALTER TABLE ONLY public.core_customuser_user_permissions DROP CONSTRAINT core_customuser_user_per_customuser_id_permission_49ea742a_uniq;
       public            yourimagine    false    217    217            �           2606    16510 F   core_customuser_user_permissions core_customuser_user_permissions_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_user_permissions
    ADD CONSTRAINT core_customuser_user_permissions_pkey PRIMARY KEY (id);
 p   ALTER TABLE ONLY public.core_customuser_user_permissions DROP CONSTRAINT core_customuser_user_permissions_pkey;
       public            yourimagine    false    217            �           2606    16494 ,   core_customuser core_customuser_username_key 
   CONSTRAINT     k   ALTER TABLE ONLY public.core_customuser
    ADD CONSTRAINT core_customuser_username_key UNIQUE (username);
 V   ALTER TABLE ONLY public.core_customuser DROP CONSTRAINT core_customuser_username_key;
       public            yourimagine    false    213            �           2606    16615     core_visarule core_visarule_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.core_visarule
    ADD CONSTRAINT core_visarule_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.core_visarule DROP CONSTRAINT core_visarule_pkey;
       public            yourimagine    false    221            �           2606    16570 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            yourimagine    false    219            �           2606    16405 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            yourimagine    false    203    203            �           2606    16403 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            yourimagine    false    203            �           2606    16395 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            yourimagine    false    201            �           2606    16591 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            yourimagine    false    220            �           1259    16457    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            yourimagine    false    207            �           1259    16453 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            yourimagine    false    209            �           1259    16454 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            yourimagine    false    209            �           1259    16439 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            yourimagine    false    205            �           1259    16511 '   core_country_country_name_b99b6c31_like    INDEX     |   CREATE INDEX core_country_country_name_b99b6c31_like ON public.core_country USING btree (country_name varchar_pattern_ops);
 ;   DROP INDEX public.core_country_country_name_b99b6c31_like;
       public            yourimagine    false    211            �           1259    16530 #   core_customuser_country_id_c3cc4fb9    INDEX     e   CREATE INDEX core_customuser_country_id_c3cc4fb9 ON public.core_customuser USING btree (country_id);
 7   DROP INDEX public.core_customuser_country_id_c3cc4fb9;
       public            yourimagine    false    213            �           1259    16543 -   core_customuser_groups_customuser_id_976bc4d7    INDEX     y   CREATE INDEX core_customuser_groups_customuser_id_976bc4d7 ON public.core_customuser_groups USING btree (customuser_id);
 A   DROP INDEX public.core_customuser_groups_customuser_id_976bc4d7;
       public            yourimagine    false    215            �           1259    16544 (   core_customuser_groups_group_id_301aeff4    INDEX     o   CREATE INDEX core_customuser_groups_group_id_301aeff4 ON public.core_customuser_groups USING btree (group_id);
 <   DROP INDEX public.core_customuser_groups_group_id_301aeff4;
       public            yourimagine    false    215            �           1259    16557 7   core_customuser_user_permissions_customuser_id_ebd2ce6c    INDEX     �   CREATE INDEX core_customuser_user_permissions_customuser_id_ebd2ce6c ON public.core_customuser_user_permissions USING btree (customuser_id);
 K   DROP INDEX public.core_customuser_user_permissions_customuser_id_ebd2ce6c;
       public            yourimagine    false    217            �           1259    16558 7   core_customuser_user_permissions_permission_id_80ceaab9    INDEX     �   CREATE INDEX core_customuser_user_permissions_permission_id_80ceaab9 ON public.core_customuser_user_permissions USING btree (permission_id);
 K   DROP INDEX public.core_customuser_user_permissions_permission_id_80ceaab9;
       public            yourimagine    false    217            �           1259    16529 &   core_customuser_username_0e60666f_like    INDEX     z   CREATE INDEX core_customuser_username_0e60666f_like ON public.core_customuser USING btree (username varchar_pattern_ops);
 :   DROP INDEX public.core_customuser_username_0e60666f_like;
       public            yourimagine    false    213            �           1259    16616 !   core_visarule_country_id_996bdb59    INDEX     a   CREATE INDEX core_visarule_country_id_996bdb59 ON public.core_visarule USING btree (country_id);
 5   DROP INDEX public.core_visarule_country_id_996bdb59;
       public            yourimagine    false    221            �           1259    16617 *   core_visarule_passport_country_id_b79dfd01    INDEX     s   CREATE INDEX core_visarule_passport_country_id_b79dfd01 ON public.core_visarule USING btree (passport_country_id);
 >   DROP INDEX public.core_visarule_passport_country_id_b79dfd01;
       public            yourimagine    false    221            �           1259    16581 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            yourimagine    false    219            �           1259    16582 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            yourimagine    false    219            �           1259    16593 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            yourimagine    false    220            �           1259    16592 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            yourimagine    false    220            �           2606    16448 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          yourimagine    false    209    2968    205            �           2606    16443 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          yourimagine    false    207    209    2973            �           2606    16434 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          yourimagine    false    2963    203    205            �           2606    16524 F   core_customuser core_customuser_country_id_c3cc4fb9_fk_core_country_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser
    ADD CONSTRAINT core_customuser_country_id_c3cc4fb9_fk_core_country_id FOREIGN KEY (country_id) REFERENCES public.core_country(id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.core_customuser DROP CONSTRAINT core_customuser_country_id_c3cc4fb9_fk_core_country_id;
       public          yourimagine    false    211    213    2984            �           2606    16533 O   core_customuser_groups core_customuser_grou_customuser_id_976bc4d7_fk_core_cust    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_groups
    ADD CONSTRAINT core_customuser_grou_customuser_id_976bc4d7_fk_core_cust FOREIGN KEY (customuser_id) REFERENCES public.core_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.core_customuser_groups DROP CONSTRAINT core_customuser_grou_customuser_id_976bc4d7_fk_core_cust;
       public          yourimagine    false    213    2987    215            �           2606    16538 P   core_customuser_groups core_customuser_groups_group_id_301aeff4_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_groups
    ADD CONSTRAINT core_customuser_groups_group_id_301aeff4_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.core_customuser_groups DROP CONSTRAINT core_customuser_groups_group_id_301aeff4_fk_auth_group_id;
       public          yourimagine    false    215    2973    207            �           2606    16547 Y   core_customuser_user_permissions core_customuser_user_customuser_id_ebd2ce6c_fk_core_cust    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_user_permissions
    ADD CONSTRAINT core_customuser_user_customuser_id_ebd2ce6c_fk_core_cust FOREIGN KEY (customuser_id) REFERENCES public.core_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_customuser_user_permissions DROP CONSTRAINT core_customuser_user_customuser_id_ebd2ce6c_fk_core_cust;
       public          yourimagine    false    213    217    2987            �           2606    16552 Y   core_customuser_user_permissions core_customuser_user_permission_id_80ceaab9_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_customuser_user_permissions
    ADD CONSTRAINT core_customuser_user_permission_id_80ceaab9_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.core_customuser_user_permissions DROP CONSTRAINT core_customuser_user_permission_id_80ceaab9_fk_auth_perm;
       public          yourimagine    false    2968    205    217            �           2606    16618 B   core_visarule core_visarule_country_id_996bdb59_fk_core_country_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_visarule
    ADD CONSTRAINT core_visarule_country_id_996bdb59_fk_core_country_id FOREIGN KEY (country_id) REFERENCES public.core_country(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.core_visarule DROP CONSTRAINT core_visarule_country_id_996bdb59_fk_core_country_id;
       public          yourimagine    false    211    2984    221            �           2606    16623 K   core_visarule core_visarule_passport_country_id_b79dfd01_fk_core_country_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.core_visarule
    ADD CONSTRAINT core_visarule_passport_country_id_b79dfd01_fk_core_country_id FOREIGN KEY (passport_country_id) REFERENCES public.core_country(id) DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.core_visarule DROP CONSTRAINT core_visarule_passport_country_id_b79dfd01_fk_core_country_id;
       public          yourimagine    false    211    2984    221            �           2606    16571 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          yourimagine    false    219    2963    203            �           2606    16576 H   django_admin_log django_admin_log_user_id_c564eba6_fk_core_customuser_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_core_customuser_id FOREIGN KEY (user_id) REFERENCES public.core_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_core_customuser_id;
       public          yourimagine    false    2987    219    213            \      x������ � �      ^      x������ � �      Z   /  x�]�K�� ��5�"'�
y���H��A�H-Dy̨�ob��η�e�Q_�/��/�a(�_�2j?��g8j�����	GK��{�U�8"X�ݿ`ǀP��&7��e�W�h�' �1��>a1��%
	���s�0�mR%·6W��cÛ�$�R�
�]�G�뾻b}ONU��c�M�sN���y��c����4�
��������'mn<�vfv��0/1{�4BP��a{��F6��->+חL��Rn-��0d_VB�'$���ͪ�9۲��1�V\~4)�1q�ؕGs�|_��*
n�      `      x��Z�v�H��_}��4��.� !��IN�I(	�����<e��gN����ԟ���} q��m<�x���7=w*"O�"�� ���?����O&����PP|����+��%�Cbu_Te�6�r�W{��\��-�3�2�g�Zu�C�+%�%�)��j���n�ύI`�[����{/�7���~>��?m;�ʛ��wt���S�̈́��K(+s02u8rLB��#��@�Du_���0���o�}��%�B� ҩ�u-�*l�z��,0YssLX�n�2Ym�r�2A�N�x�+f�m����Uy��^�a�Y�S1����T��Y�K	B���n���^���m�?$KLE(��s:�Țj��<+��1�^F���\�G6ѻ_�zJ�6'�4��*�wE���XNYdY<6y�y:YrL� D0Xr*н{z����ͪh���Y]/�=����z�,ɂ9c��{q��i�+���}�'dO�1����a�R�-[*d���ĳU���3���)c�҆���j[�Z1!�8�f�0~N�L��R/�D`�oSiē� ��6��+���	b������Ԑ��zl�Z��,�_uG��5�f�J��n<c÷<�L�do�_�j[B�0���s��`�9SB�nժ�9��L����tk�R�m�o�=ȯ6�Vi}\��pB[�����U��Z6\y����9�MuDF*����~�8}�m�P��"�ے^�R��ڭ��d <#\��f�0:���}^�����A}��!7c"tL�D�c7�K�����7��X��l�[�+��3�Iv2#{�6�����+�t��k��?wh����H�E+��wK�١�O�hwR�-c���M�9Xq�����D�"�����^`��z~��i���N�y�'����&k(�dV���,���[�=��R�񷙆`�l�L([�w���M6���Vp�Kf��S�o��Ů���c��iS� ��*$Q�{��?�w�� ����%bN�~8���;�:��8��R� %p����Y�����X���1�B2��M�9��!d#�֜�#��V��≱����$��ͪx*������ۺBq쟾>�D��f,�䰓�����`![y �y��*o!�F�@�У��*��j��߭ۀ4�9����gĶ���3%��_8��͹����E՘�@�Zq�����]�nu�Y$��М�5P�R��3#G��>�ߋ���T/�AK���_�,Fh'ۛ�RFrd
���|���Q�ɹ��S��&��V�lv���3��^�rw��Z�ˎ�̕�J����j�X�芤��Pܾ�Gc��"I�	�tlk� f���I$K���t0#=�I�����������$�1����H
r��o��e�P�
|hA����_��t@R�1��hO-�rH2�zq���d��>��/�VY�/{9�q�Y-�P@���l�4�Ͼt�R�� b���>M��&��s�Zm$>��fR�<�̉��2��1M<�Τ&�&�o'9��Q!ў�����EdKn�:M�WF�h�+7����[�$��i�@�HXqɑ_Z^�Gu�R*x�}Y���1$�7���q5B?��Dnh�Hm�?����\+�D����W��B]���11t�ir�r�.����r=�LA*�%�7�&ۼ:R��G���wDOV�ug�5�������\��H�A��A�%X78���!3�x���#�O%�+�`L?��]���Մc8�f�\���Z(D���E�.��-#d��s��M!|]�G3��by�3�Y����-S�ڨ{��3+��\�h*P�Ҵ&���\�ݧ����o��;�)���0�ŀ�p	CK��ș8ǆCpE��������/e��������M}&�
@���d�K�fJ���	M�v���<[֖�W���uHb�zYuLuQ�O�"o}׀�/E') ntǍ�{NB��C}�Xz�!�?������ q�S��jp�*;K��c�G<@����x#7/���e��2\3�����������e������*$5�C�{�y��<_�����9Y��k�u��׹�XY@��"�ή&ԺEw� �}-�ѵ|Ǎz �ױrx$�k�כꮑ摬��}���>z�O������S'��/���'H�_��>xyTY�k����g�������#O�U����@������6�p����n�:�ټ�z��p£��?�jN��#�9���9��2�[^nO,ɼLR�b�Hǅt\Mz��">��k�z��`�-�/��1����&(��L�=������)A���\�f��| u�N��fB��lˮ�O�g�烁�(@Rʛ����Հ9̷�`Q�=���v�RNe�S�0�� �&���OOG���x�4�.��,{� ���&Δ�?�9�(6d�'��Q�|��v	��᪮��$V���"sc�ٱ-���LNq�F��!ҥ+��:.���%�}��lH�z�{ęn�QX����݆�����/\h���znN��0�ew���x3�U��(�q���|�_�0V��� �C.1���Y��JOE�T�!��kI�č!)���LR��~6)+&C�V+7T)(�xw���;����
kbq�*����8oY�8M����%�����17~�(,�v�Uz���'��>���Hx�t�3:]��s��rN<{-��(�B'�p���|���v�@H� �t����1��H�a�������%s�����>���W5�Fi��!D2�Qa�B���m�۵��o��m�r������:��\'�ʎ�.!������}Wa����L$���g���/G����:��9�a��MyZrG���"л��8��(J���>�82!`�H2�8��(8���Grn�"hBEv�*<��2�R�������"=`a��J�*�_��l���Mn�/[ �< �v�R��ߗ�����21�=��#����H�b5��������g\= gi�Y���8�#Q�KUc�\,�y�t�Ts=�L|.�������H���$�J|�d�|ڞV��̰ �$����1sH� ')ѐ�#:� 2�0�l܀,������^��?�Ll{В���S�K�,�4ư@Z Y����� �	��Co:�M�^�%	�iE� t'S�C�a�/��^@���ڂ��Ď~`����lh ����ͶKz��	 s၉:��@�	 ^�1`�u�����E2�ʣ
 X����`E��p�bK�'�8�m��Զ!0���b�0�^t|�2���n�@{��р&��A`��T�_�XȒ�?��pAV�ow�g�� ��U*'�C�T�m8°�h*HO#PB:>3��
��q�4���{i��Er�0�~|
��nF��E������4%���t�����	�݌H<d,٠e�.ԥ�31�@�̀��C#���,��fv�ý�&5��sd���������ע�aQLa�lp�F�ͦaʑ�%�t
��9���e>����x8�;>��0k���ت�;�6�5�wx�~��hi��N�F�G��nN��	� hì�H/l�6V.�o�R�QH4��5�B�DqD@� >Vx�y&����^���u��.Gɚ�:40�nlV aN�v6�?���	L�]>���?��������W�@���`���i�竘�W\&н���6-�wy����	l_O���h	�_B�*����ox����	7���9s��,���X��j?���k־�"6;�^��;�f�M��_��;ӄJ�g`E�^�!7�ן�c1�Q^u%����^_Մ��;�P������_珧�Pߌ�^Qͩ�u�8���)	Lz��3�%=_�F����}��a���#�G��%| ��=�\�_Ͻt�Ԇ ������#yA��pj�� �E<W��&�z*�9.Qq��t����@�<5�7��og�=�޾�I�}Pm������������KF4�ҥ o   i���&�Zp�O�T4��W4ۮ@�����$��# ���S
zﳋ�|�EX���d6��`�Oc���_Ps���!SF�#Jc��?JS&�쮾9�S����%ƔBn���R�Rح˧��:�23��7X���������Ws�wE�����0�y�㢺&�>������&g�4���:��b@}�(���j��0h@�(���S�)��!�-ebJ���+̧����jo���j���A���P���v��|��!�2�@��'^S�t�b^�^�X���Msp�ν��!r�24�;h�^�����4�����v�~C���}��X������7���|Ȁ$��w���3�xL�y��--�w|����{P�_�=h&�L�Ͳ4�Y��u�CB~�KX�~��R�ӎ�0��4_'�ψf�L볈�A��"��%���>#��)]�!]��~ѿ|���1bLs^��~�*.x���]М#����/*���Csԣ�����hQ��bsdR}�Z�9-��K��C>sԧ�Z�B�Y�в|��o���I�����k`�{��4=ʣ���sD�+�<��_~���ק�      b   �   x�m��
�@ ϟO��[d�mjdI��-� �\WI�ܖ|��ss��� ��{��Ee�ؤH:̌)嵔�����$`AʥY��ZD�p����v�Ĳ�����M�o�
��1>S5$��l��8!�d�Zd�Q��	�� p!�z�G��b&��nU����C��+�Es�=j�-�0>�>7X      d      x������ � �      f      x������ � �      j      x������ � �      h      x������ � �      X   e   x�M��
�@�ϓ�l���i]��,�s���X/!	_���ɩ�WV.�;��oTYs2KR��7�JT�������^d|,�2��$���a.9�s��8-X      V   �  x����n� ���StՊ�>˕J����vԼ}��$Rm9[2>̙3�����tm: �@��M��F��"�
��;#� oQ��?�����h�p�zY�eE���( &EA�����'6���"�M���z��w)�0�uo���C��Z%1�))(�PdA�)?lo�ߧ0��Px��GJy��qJ����!�="�I���s���o����Axn���b�Fm�.�m0��0Tc�� ���L!&m�gmcQ�6%�ٍ�H\{���5{�y5�����BIF�(�������9��)h���-�z��������O�2�Ǫ>\|�,���V�3�� 1���$9���Oh$"�N>���l�t�����jB���+�m,�r��|��T��ÛN�>�;m��)"��Z�8�}���!U��z��&%��k����vC#P}���\\2q��GR�:��]b�� j��������Ö      i   �  x�=�����E��<���÷#%�I� �$�f�|zk`��^��:�s	��k0�p�O�
��	O�~#g�)����7��(oƲ��6f�-���T1F��ٲS@Z�,M�����犑�D�8M�aN�3&��2w�A��iV6M*id��c�^��)z���-�Wl���,�.۬����\cT��A�R�n����'�>��?�t$���`�(i��կ�X�=m�ٲ���7g�uq	Y��B��>�7L�����!B�A��,�:j[�PI�ز�-����ޱ���]�	��4@�E�e��q���٤��\Ժ�]����H:��$� ��Z���'�H��p�6C|i^��V����(��(��rP�D]f�>�[X���ϸ�X��`D�ۢ������^W�Yk��Nr��[�W�2h�\����{�~�!���s؞��V�fϸ�3�L���x�ۍ�M���B6�ɨ�bۄ*�E���d��ʄp���!�f�p��panS����������<�zIѹg�2i���!ݻ���&?���;��)^���Gh�)�Ɇ'�{y�5v�0��9��>(bOd�+�K�l�ck��v�S��r�a_(� z�feX�U��M�*0јz��Q51[Hn�u��Ƣ���G�ab�����(�W�WF>�ɨ�3���h�8���Sr�Elc�ߝ;�IM|��|!E�p�Z�a��t�W	�f�$v%ǋ��?�9��D�|�u�ʍ�`����y8�{�	sFΔ�JZ�t��?�(��ҍ�`�Fp�K8�t�`�ءx����;M�k����/���#�ܑ;g"V�V"�@��:W�k_n������;*G�����l��GD���
7�=����Av�)��J��?&;q�%ld�-�f��+v�ټ;�߿��'�;$������h����v��&�Z{ڹ8u�����
%α��a�U��2��#�o��Z^��_��A�8��Mo,�/#q��(��g��
aQ�g<
d��ߍ%>m],���hV�Ĉ	i	�?@�Kd�FAԕ���ꖛ�< Z57��rP��������>σ���(l�"J� k��y�DHva���z:�c*O8GY�^�6�h��4�eZ�	��|�qn�I����u��d�����F�u=ENd�+4e�����vC�7��U	D��X��a]�8LB��q���E�"����s����2ͺ����eB�C>+�7ߐ>�˽�C�!pJsL���Q�9��'M�DY���9:B�F���85������� :e��b%�]6��T�a**;��U4"xm�p`���z�6D*-��h�7�/��<6.��*����]�^�#Nw3Z�����M�4�+�%Z�C%��3~���MD��LW�S�L�JV%��Re{ U������$VV��i%jJnp�l�3}����W�{C����8k��0��M�l��@�
���	JI�b'`��V��m3�k�-���I�'gd2L������j�Zy�@R!'p��&�-�=�#�D)�W12�*h-S����g��^�r?��g�����T�@�	�?�o�$'�+�����i��l�c]bBNL�{Z��Š�a�:�=ɠI��Ͳ0ʠ"�eǝU4��2,eg��)�˜y�6%[9�g��{�
�i������YΦG�g�����h�U�t��?K.���NJ֑��W촡�����Vr���M'��o!��L�nAs���7j^�j!p�VD�U��FC>���J^Z�f�$i�,I�fq�§�rjO��<���A����~5����m8nJkN�׭�b�0-�^��x�L����R�n��-P����hf�h��!%0LgV��z)�tb�v��7d��.b�5�w}�k�I�A��%$��Ҍ�l��mgv�^���l&�!5���x{I�U��,���C����(�4�G��?����O�p=C��a�����ؽ�/�O4�~1~�p��f\b����C��s��ϻ�'���|-fp%�0��g*+��4��E	���LQ�ŉ�{�R\҅-��1��,��J*c����{��?�c���4N*����*a~�N<��u�t~-m댛��$���p�bY=>�D���9{@�o�
����I��_'��ϯ_���6��     