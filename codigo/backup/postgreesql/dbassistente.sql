PGDMP     (                    {            postgres    15.3    15.3     
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    5    postgres    DATABASE        CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE postgres;
                postgres    false                       0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    3341                        3079    16384 	   adminpack 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;
    DROP EXTENSION adminpack;
                   false                       0    0    EXTENSION adminpack    COMMENT     M   COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';
                        false    2            �            1259    16403 	   entidades    TABLE     h   CREATE TABLE public.entidades (
    nome text NOT NULL,
    entidades text NOT NULL,
    flagdb text
);
    DROP TABLE public.entidades;
       public         heap    postgres    false            �            1259    16415    funcoes    TABLE     Q   CREATE TABLE public.funcoes (
    funcao text,
    tipo text,
    codigo text
);
    DROP TABLE public.funcoes;
       public         heap    postgres    false            �            1259    16398 	   intencoes    TABLE     J   CREATE TABLE public.intencoes (
    intencao text,
    enunciados text
);
    DROP TABLE public.intencoes;
       public         heap    postgres    false                       0    0    TABLE intencoes    COMMENT     m   COMMENT ON TABLE public.intencoes IS 'tabela para armazenar intencoes e suas utterances (formas de chamar)';
          public          postgres    false    215            �            1259    16410    relacoes_intencoes_entidades    TABLE     t   CREATE TABLE public.relacoes_intencoes_entidades (
    chave_intencao text,
    chave_entidade text,
    db text
);
 0   DROP TABLE public.relacoes_intencoes_entidades;
       public         heap    postgres    false            �            1259    16420    relacoes_intencoes_funcoes    TABLE     c   CREATE TABLE public.relacoes_intencoes_funcoes (
    chave_intencao text,
    chave_funcao text
);
 .   DROP TABLE public.relacoes_intencoes_funcoes;
       public         heap    postgres    false                      0    16403 	   entidades 
   TABLE DATA           <   COPY public.entidades (nome, entidades, flagdb) FROM stdin;
    public          postgres    false    216   =                 0    16415    funcoes 
   TABLE DATA           7   COPY public.funcoes (funcao, tipo, codigo) FROM stdin;
    public          postgres    false    218   r                 0    16398 	   intencoes 
   TABLE DATA           9   COPY public.intencoes (intencao, enunciados) FROM stdin;
    public          postgres    false    215                    0    16410    relacoes_intencoes_entidades 
   TABLE DATA           Z   COPY public.relacoes_intencoes_entidades (chave_intencao, chave_entidade, db) FROM stdin;
    public          postgres    false    217   ?                 0    16420    relacoes_intencoes_funcoes 
   TABLE DATA           R   COPY public.relacoes_intencoes_funcoes (chave_intencao, chave_funcao) FROM stdin;
    public          postgres    false    219   p          %   x�K�+�O-.�/,M�,K����I�,������� ��	p         �   x���
�0@��+J&���Zp*��S�\��ZOJ.������7�)��vm��H��9��a��#��q;�f��|F���B�/�c`�����n)	$9�����y��)�'S�_��&���S�3���R�v�X��a��Gu�J��:            x�K-.�/,M�L��\1z\\\ X5�         !   x�K-.�/,M�,K����I�,������� w��            x�K-.�/,M�L+�KN����� Fk�     