# Data Pipeline for drone data
A city traffic department wants to collect traffic data using swarm UAVs (drones) from a number of locations in the city and use the data collected for improving traffic flow in the city and for a number of other undisclosed projects. this project objective is for creating a scalable data warehouse that will host the vehicle trajectory data extracted by analysing footage taken by swarm drones and static roadside cameras



## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Contact](#contact)

## General info
The data warehouse should take into account future needs, organise data such that a number of downstream projects query the data efficiently. You should use the Extract Load Transform (ELT) framework using DBT.  Unlike the Extract, Transform, Load (ETL), the ELT framework helps analytic engineers in the city traffic department setup transformation workflows on a need basis

## Screenshots
![Example screenshot](./img/techstack.png)

## Technologies
* Airflow
* Postgres
* DBT

## Setup
To copy and follow the same procedures go check out my [blog](https://medium.com/@smlalene/data-warehouse-tech-stack-with-postgresql-dbt-airflow-35dfb7e743f8)


## Features

- sends email when dags fail
- dbt docs is deployed at https://musical-entremet-44e5bc.netlify.app/


To-do list:
- add more dags and transformations
- add more dbt packages data control montoring
- add tests

## Status
_finished_



## Contact
Created by Samuel Alene - feel free to contact me!