CREATE TABLE "inproceedings" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT,
  "title" TEXT,
  "year" integer,
  "booktitle" TEXT,
);

CREATE TABLE "books" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT,
  "title" TEXT,
  "year" integer,
  "publisher" TEXT,
  "editor" TEXT,
  "volume" integer,
  "number" integer,
  "pages" TEXT,
  "month" integer,
  "note" TEXT,

);

CREATE TABLE "articles" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT,
  "title" TEXT,
  "journal" text,
  "year" integer,
  "volume" integer,
  "pages" TEXT,
);

