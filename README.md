# 🏋️ Exercise Lookup API

A lightweight, RESTful API built with FastAPI that allows users to search and filter exercises based on **muscle group**, **equipment**, or both. Ideal for fitness apps, workout builders, or personal trainers building custom tools.

---

## 📚 Features

- 🔍 Search exercises by muscle group (`chest`, `back`, etc.)
- 🛠️ Filter by equipment used (`dumbbell`, `barbell`, `bodyweight`, etc.)
- 🧾 JSON responses for easy integration

---

## 📥 Endpoints

### `GET /exercises`

**Query Parameters (optional):**

| Parameter   | Type   | Description                        |
|-------------|--------|------------------------------------|
| `muscle`    | string | Filter by muscle group             |
| `equipment` | string | Filter by equipment used           |

**Example Request:**

```http
GET /exercises?muscle=chest&equipment=dumbbell
```

**Example Response:**
```http
[
  {
    "id": 29,
    "name": "Push-up",
    "muscle": "Chest",
    "equipment": [
      "Bodyweight"
    ],
    "difficulty": "Beginner",
    "type": "Strength"
  },
  {
    "id": 32,
    "name": "Bench Press",
    "muscle": "Chest",
    "equipment": [
      "Barbell",
      "Dumbbell"
    ],
    "difficulty": "Intermediate",
    "type": "Strength"
  }
]
```