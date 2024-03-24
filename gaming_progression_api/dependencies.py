from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException

from gaming_progression_api.services.unitofwork import IUnitOfWork, UnitOfWork
from gaming_progression_api.settings import get_settings

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
