package com.pims.api.models;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;
import java.sql.Date;
import java.util.List;

@Entity(name="Health")
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler"})
public class Health {
    @Id
    //private String ssn;
    private Character sex;
    private Date date_of_birth;
    private Date date_of_death;

    @OneToOne
    @JoinColumn(name = "ssn")
    @JsonBackReference
    private Population population;

    public Health(){}

    public String getSsn() {
        return population.getSsn();
    }

    public void setSsn(String ssn) {
        this.population.setSsn(ssn);
    }

    public Character getSex() {
        return sex;
    }

    public void setSex(Character sex) {
        this.sex = sex;
    }

    public Date getDate_of_birth() {
        return date_of_birth;
    }

    public void setDate_of_birth(Date date_of_birth) {
        this.date_of_birth = date_of_birth;
    }

    public Date getDate_of_death() {
        return date_of_death;
    }

    public void setDate_of_death(Date date_of_death) {
        this.date_of_death = date_of_death;
    }

    public Population getPopulation() {
        return population;
    }

    public void setPopulation(Population population) {
        this.population = population;
    }
}
