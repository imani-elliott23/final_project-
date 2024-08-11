document.addEventListener('DOMContentLoaded', function() {
    fetchWorkouts();

    async function fetchWorkouts() {
        const response = await fetch('/workouts');
        const workouts = await response.json();
        const workoutsContainer = document.getElementById('workouts-container');
        let workoutList = '<ul>';

        workouts.forEach((workout, index) => {
            workoutList += `
                <li>
                    ${workout.date} - ${workout.exercise} for ${workout.duration} mins
                    <button onclick="deleteWorkout(${index})">Delete</button>
                </li>
            `;
        });

        workoutList += '</ul>';
        workoutsContainer.innerHTML = workoutList;
    }

    window.deleteWorkout = async function(index) {
        const response = await fetch(`/delete_workout/${index}`, {
            method: 'DELETE'
        });
        if (response.ok) {
            fetchWorkouts();
        } else {
            alert('Failed to delete workout');
        }
    }
});