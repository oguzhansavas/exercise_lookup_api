from fastapi import FastAPI, HTTPException
from typing import List, Optional
from app.data import exercises

app = FastAPI(title="Exercise Lookup API")

@app.get("/exercises", response_model=List[dict])
def get_exercises(muscle: Optional[str] = None, equipment: Optional[str] = None):
    results = exercises
    if muscle:
        muscle_list = [m.strip().lower() for m in muscle.split(",")]
        results = [
            ex for ex in results
            if any(m in [x.strip().lower() for x in ex["muscle"].split(",")] for m in muscle_list)
        ]
    if equipment:
        equipment_list = [e.strip().lower() for e in equipment.split(",")]
        results = [
            ex for ex in results
            if any(eq in [x.strip().lower() for x in ex["equipment"].split(",")] for eq in equipment_list)
        ]
    return results
