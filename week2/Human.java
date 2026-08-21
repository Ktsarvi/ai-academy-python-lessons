import java.time.LocalDate;

public class Human {
    private String name;
    private String surname;
    private LocalDate dateOfBirth;
    private Integer height;

    public Human(String name, String surname, LocalDate dateOfBirth, Integer height) {
        this.name = name;
        this.surname = surname;
        this.dateOfBirth = dateOfBirth;
        this.height = height;
    }

    public String walk() {
        return "walking";
    }

    public String eat() {
        return "eating";
    }

    public String sleep() {
        return "sleeping";
    }
}

public class Teacher extends Human {
    private String subject;

    public Teacher(String name, String surname, LocalDate dateOfBirth, Integer height, String subject) {
        this.name = name;
        this.surname = surname;
        this.dateOfBirth = dateOfBirth;
        this.height = height;
        this.subject = subject;
    }

    public String teach() {
        return "teaching";
    }
}

public class Student extends Human {
    private String major;

    public Student(String name, String surname, LocalDate dateOfBirth, Integer height, String major) {
        this.name = name;
        this.surname = surname;
        this.dateOfBirth = dateOfBirth;
        this.height = height;
        this.major = major;
    }

    public String study() {
        return "studying";
    }
}

public class Developer extends Human {
    private String programmingLanguage;

    public Developer(String name, String surname, LocalDate dateOfBirth, Integer height, String programmingLanguage) {
        this.name = name;
        this.surname = surname;
        this.dateOfBirth = dateOfBirth;
        this.height = height;
        this.programmingLanguage = programmingLanguage;
    }

    public String code() {
        return "coding";
    }

    public String drinkCoffe() {
        return "drinking coffee";
    }
}

var javid = new Human()