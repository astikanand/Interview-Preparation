public class JobOpening {
    String  jobTitle = "Give your Job Title";

    public Candidate hireCandidate () {
        if (lookingForJob) {
            applyForJob(jobId);
        } else {
            System.out.println("Thank you for looking at my email");
            System.out.println("Save my contact for future purposes");
            System.out.println("Have a good day!");
        }

        if (notInterestedNow) {
            System.out.println("Please refer someone who you think can match your expertise");
            saveMyContact();
        }

        if (mindChanged && wantToApply) {
            applyForJob(jobId);
        }

        return new Candidate();
    }

    public void applyForJob(jobId) {
        String jobDescriptionLink = "link for the JD";
        System.out.println("Review the Job description by clicking above link! for " + jobId);
    }

    public void saveMyContact() {
        System.out.println("Milind Dadape >> +91-9885004723  >> milind.dadape@cotiviti.com")
    }

}





