from fastapi import FastAPI, Query
from typing import List, Optional
from app.models import Exercise
from app.data import exercises

app = FastAPI()

@app.get("/exercises", response_model=List[Exercise])
def get_exercises(
    muscle: Optional[str] = Query(None, description="Comma separated muscle groups"),
    equipment: Optional[str] = Query(None, description="Comma separated equipment"),
    difficulty: Optional[str] = Query(None, description="Difficulty level")
):
    results = exercises

    if muscle:
        muscle_list = [m.strip().lower() for m in muscle.split(",")]
        results = [
            ex for ex in results
            if any(m in ex["muscle"].lower() for m in muscle_list)
        ]

    if equipment:
        equipment_list = [e.strip().lower() for e in equipment.split(",")]
        results = [
            ex for ex in results
            if any(eq in (item.lower() for item in ex["equipment"]) for eq in equipment_list)
        ]

    if difficulty:
        diff = difficulty.strip().lower()
        results = [
            ex for ex in results if ex["difficulty"].lower() == diff
        ]

    return results
