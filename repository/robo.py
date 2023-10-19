from sqlalchemy.orm import Session
from fastapi import Header, Depends

import models

def get_tenant_id(tenant_id: str = Header(None)):
    """
    The function `get_tenant_id` returns the value of the `tenant_id` parameter.
    
    :param tenant_id: The `tenant_id` parameter is a string that represents the ID of a tenant. It is an
    optional parameter that can be passed as a header in an HTTP request
    :type tenant_id: str
    :return: The tenant_id is being returned.
    """
    return tenant_id


def get_categories_and_questions(db: Session, tenant_id: str = Depends(get_tenant_id)):
    """
    The function retrieves categories and their associated questions from a database and returns them in
    a structured format.
    
    :param db: The parameter `db` is of type `Session`. It is expected to be an instance of a database
    session, which is used to interact with the database and perform queries
    :type db: Session
    :return: The function `get_categories_and_questions` returns a list of dictionaries, where each
    dictionary represents a category and its associated questions. Each category dictionary contains the
    following keys:
    """
    categories = db.query(models.Question_Category).all()

    categories_with_questions = []

    for category in categories:
        category_data = {
            "categoryId": category.id,
            "categoryName": category.category_name,
            "questions": []
        }

        questions = db.query(models.Question_List).filter(models.Question_List.category_id == category.id).all()

        for question in questions:
            question_data = {
                "questionId": question.id,
                "questionName": question.question,
                "questionType": question.question_type
            }

            if question.question_type == "mcq":
                responses = db.query(models.Response_List).filter(models.Response_List.question_id == question.id).all()

                response_list = []
                for response in responses:
                    response_data = {
                        "answerId": response.id,
                        "answer": response.response_name
                    }
                    response_list.append(response_data)

                question_data["responseList"] = response_list

            category_data["questions"].append(question_data)

        categories_with_questions.append(category_data)

    return categories_with_questions
