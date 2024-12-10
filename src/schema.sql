CREATE TABLE "inproceedings" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT,
  "title" TEXT,
  "booktitle" TEXT,
  "year" integer,
  "editor" TEXT,
  "volume" integer,
  "number" integer,
  "series" TEXT,
  "pages" TEXT,
  "address" TEXT,
  "month" TEXT,
  "organization" TEXT,
  "publisher" TEXT,

);

CREATE TABLE "books" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT[],
  "title" TEXT,
  "year" integer,
  "publisher" TEXT,
  "editor" TEXT[],
  "volume" integer,
  "number" integer,
  "pages" TEXT,
  "month" TEXT,
  "note" TEXT,

);

CREATE TABLE "articles" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT,
  "title" TEXT,
  "journal" text,
  "year" integer,
  "volume" integer,
  "number" integer,
  "pages" TEXT,
  "month" TEXT, 
  "note" TEXT,
  
);

