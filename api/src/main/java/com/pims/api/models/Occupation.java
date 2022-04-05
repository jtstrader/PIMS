package com.pims.api.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;

@Entity(name="Occupation")
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler"})
public class Occupation {
    @Id
    private String ssn;
    private Integer business_id;
    private String position;
    private Integer wage;
    private Integer salary;

    @ManyToOne
    @JoinColumn(name = "ssn")
    private Population population;

    @ManyToOne
    @JoinColumn(name = "business_id")
    private Business business;

    public Occupation(){}

    public String getSsn() {
        return ssn;
    }

    public void setSsn(String ssn) {
        this.ssn = ssn;
    }

    public Integer getBusiness_id() {
        return business_id;
    }

    public void setBusiness_id(Integer business_id) {
        this.business_id = business_id;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public Integer getWage() {
        return wage;
    }

    public void setWage(Integer wage) {
        this.wage = wage;
    }

    public Integer getSalary() {
        return salary;
    }

    public void setSalary(Integer salary) {
        this.salary = salary;
    }

    public Population getPopulation() {
        return population;
    }

    public void setPopulation(Population population) {
        this.population = population;
    }

    public Business getBusiness() {
        return business;
    }

    public void setBusiness(Business business) {
        this.business = business;
    }
}
