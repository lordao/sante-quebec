# Product Development Hiring Project

This outlines a recent problem we ran into and came up with a development solution for. We'd like to see how you would handle it. What is most important is gaining some insight into your development process and seeing how you work.

## Background

[BriteCore](http://www.britecore.com/) is a web-based platform insurance companies use to manage their business. Insurance is a form of risk management. Risks are anything that someone could incur a loss on. BriteCore has historically worked primarily with property-based risks (homes, farms, churches, etc.).

## Problem

Since BriteCore was created to work mostly with property-based insurance, the data model is pretty rigid. The data model assumes that all risks are properties and have addresses. This makes it difficult for BriteCore to work with different forms of insurance like Automobile Policies, Cyber Liability Coverage (protection against hacking), or Prize Insurance (if someone gets a $1 million hole-in-one prize at a golf tournament, the golf course doesn't pay it, they have an insurance policy to cover them).

## Primary Goal

We would like to see you come up with a solution that allows insurers to define their own custom data model for their risks. There should be no database tables called `automobiles`, `houses`, or `prizes`. Instead, insurers should be able to create their own risk types and attach as many different fields as they would like.

Fields are bits of data like first name, age, zip code, model, serial number, Coverage A limit, or prize dollar amount. Basically any data the carrier would want to collect about the risk. Fields can also be of different types, like text, date, number, currency, and so forth.

### Data

For the data layer, model the risk types and how the generic fields and field types would relate to these risk types. Field types should be either `text`, `number`, `date`, or `enum` (where there are multiple potential options but only one choice can be made).

Deliverables will be either...

1. A Python file containing the ORM classes for these tables.
2. An entity relationship diagram, which depicts the tables and their relationship to one another.
3. Both 1 and 2, because you're awesome.

### Backend

For the backend, create two API endpoints. One that returns a single risk type and one that returns a list of all risk types. Include all of the risk types' fields, field types, and any other data about the fields. This is your chance to show that you know how to create clean REST APIs.

Deliverables will be...

1. A well-tested REST API written in Python. **Bonus points** if you use Django.

### Frontend

The frontend is all about collecting information as it relates to these generic models. Create a single page that hits your risk type API endpoint(s) and displays all of the fields to the user in a form. Be sure to display at least one field of each type on the page. Don't worry about submitting the form.

Fields should use appropriate widgets based on their type. `text` fields should display as text boxes, `date` fields should use date pickers, and so on.

Deliverables will be...

1. A modern JavaScript app. **Bonus points** if you use ES6 and a modern JavaScript framework. **Mega bonus points** if you use Vue.js specifically.

## Questions

For questions, please use the contact email you were provided in the hiring step that brought you to this repo.

## Finished?

When you're done with the above project, please submit your GitHub repo to the contact email you were provided in the hiring step that brought you to this repo. Include with that a link to a live hosted instance. If you haven't already supplied a resume during this process, attach it to your email.

1. **Bonus points** if you also orchestrate the launch environment in AWS using CloudFormation.
2. **Mega bonus points** if you host the app in [AWS Lambda](https://aws.amazon.com/lambda/) using [Zappa](https://github.com/Miserlou/Zappa) or [AWS ECS](https://aws.amazon.com/ecs/) using [AWS Fargate](https://aws.amazon.com/fargate/).

## Evaluation

If you'd like to do very well on this project, we'll hand you the categories we utilize to score candidates! They are:

1. Business requirements are met or exceeded
2. Documentation is clearly written
3. Django is PEP8 compliant and avoids antipatterns
4. Vue.js contains appropriate ViewModels and DOM interactions
5. CSS Framework is utilized correctly
6. Test coverage is complete and meaningful
7. Deployment is fully scripted
8. Communication is positive and respectful
