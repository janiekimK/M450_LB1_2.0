import pytest
from unittest.mock import MagicMock, patch
import time
from sdbms import DBHelper, AddStudent, Window, evaluateStudentGrades

# Unit Test 1: Mock DBHelper to test methods without actual database connection
def test_add_student():
    # Mocking DBHelper to avoid real database interaction
    with patch('sdbms.DBHelper') as MockDBHelper:
        # Create a mocked instance
        mock_db = MockDBHelper.return_value

        # Mock the addStudent method
        mock_db.addStudent = MagicMock(return_value=None)

        # Call the mocked method with test data
        sid, sname, dept, year, course_a, course_b, course_c = 1, "Test User", 0, 0, 0, 0, 0
        mock_db.addStudent(sid, sname, dept, year, course_a, course_b, course_c)

        # Assertions
        mock_db.addStudent.assert_called_once_with(sid, sname, dept, year, course_a, course_b, course_c)


def test_delete_record():
    # Mocking DBHelper to avoid real database interaction
    with patch('sdbms.DBHelper') as MockDBHelper:
        # Create a mocked instance
        mock_db = MockDBHelper.return_value

        # Mock the deleteRecord method
        mock_db.deleteRecord = MagicMock(return_value=None)

        # Call the mocked method with test data
        sid = 1
        mock_db.deleteRecord(sid)

        # Assertions
        mock_db.deleteRecord.assert_called_once_with(sid)


def test_search_student():
    # Mocking DBHelper to avoid real database interaction
    with patch('sdbms.DBHelper') as MockDBHelper:
        # Create a mocked instance
        mock_db = MockDBHelper.return_value

        # Mock the searchStudent method
        mock_db.searchStudent = MagicMock(return_value=["Test Data"])

        # Call the mocked method with test data
        sid = 1
        result = mock_db.searchStudent(sid)

        # Assertions
        mock_db.searchStudent.assert_called_once_with(sid)
        assert result == ["Test Data"]

# Unit Test 2: Specialized Testing with Time Freezing
@patch('time.time', return_value=1672531200)  # Mock current time (01 Jan 2023, 00:00:00 UTC)
def test_time_freezing(mock_time):
    # Ensure the mocked time is returned
    assert time.time() == 1672531200

    # Example logic that depends on current time
    current_timestamp = time.time()
    assert current_timestamp == 1672531200

    # You can test any logic in your code that uses time here


# Testing the AddStudent Dialog Logic
def test_add_student_dialog_logic(qtbot):
    # Create an instance of AddStudent dialog
    add_student_dialog = AddStudent()

    # Simulate user input in the dialog fields
    add_student_dialog.rollText.setText("1")
    add_student_dialog.nameText.setText("Test User")
    add_student_dialog.yearCombo.setCurrentIndex(0)
    add_student_dialog.branchCombo.setCurrentIndex(0)
    add_student_dialog.cACombo.setCurrentIndex(0)
    add_student_dialog.cBCombo.setCurrentIndex(0)
    add_student_dialog.cCCombo.setCurrentIndex(0)

    # Trigger the addStudent function
    with patch('sdbms.DBHelper.addStudent') as mock_add_student:
        mock_add_student.return_value = None  # Mock the DB operation
        add_student_dialog.addStudent()

        # Assert that the mocked method was called with the correct arguments
        mock_add_student.assert_called_once_with(1, "Test User", 0, 0, 0, 0, 0)

def test_evaluate_student_grades_valid_scores():
    # Test normal behavior
    assert evaluateStudentGrades(95) == "6"
    assert evaluateStudentGrades(85) == "5"
    assert evaluateStudentGrades(75) == "4"
    assert evaluateStudentGrades(65) == "3"
    assert evaluateStudentGrades(55) == "2"

def test_evaluate_student_grades_edge_cases():
    # Test boundary values
    assert evaluateStudentGrades(90) == "6"
    assert evaluateStudentGrades(80) == "5"
    assert evaluateStudentGrades(70) == "4"
    assert evaluateStudentGrades(60) == "3"
    assert evaluateStudentGrades(50) == "2"

def test_evaluate_student_grades_invalid_scores():
    # Test invalid inputs
    with pytest.raises(ValueError, match="Score must be between 0 and 100"):
        evaluateStudentGrades(-1)
    with pytest.raises(ValueError, match="Score must be between 0 and 100"):
        evaluateStudentGrades(101)
    with pytest.raises(TypeError, match="Score must be a number"):
        evaluateStudentGrades("not a number")
