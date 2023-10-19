from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
from repository import robo

router = APIRouter(
    tags=['Robo']
)


get_db = database.get_db


@router.get('/roboadv/ra-pf/api/v1/ra/get-qa/')
def get_categories_and_questions_api(db: Session = Depends(get_db)):
    """
    The function `get_categories_and_questions_api` retrieves categories and questions from a database
    using the `robo.get_categories_and_questions` function.
    
    :param db: The parameter `db` is of type `Session`. It is expected to be a database session object
    that is used to interact with the database
    :type db: Session
    :return: the result of the `robo.get_categories_and_questions(db)` function call.
    """
    return robo.get_categories_and_questions(db)