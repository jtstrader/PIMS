package com.pims.api.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;
import java.util.List;

@Entity(name="Population")
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler"})
public class Population {
    @Id
    private String ssn;
    private String first_name;
    private String last_name;

    @OneToMany(mappedBy = "population")
    private List<Occupation> occupations;

    @OneToMany(mappedBy = "population")
    private List<Location> locations;

    @OneToOne(mappedBy = "population")
    private Health health;

    @OneToOne(mappedBy = "population")
    private MaritalStatus maritalStatus;

    public Population(){}

    public String getSsn() {
        return ssn;
    }

    public void setSsn(String ssn) {
        this.ssn = ssn;
    }

    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }

    public List<Occupation> getOccupations() {
        return occupations;
    }

    public void setOccupations(List<Occupation> occupations) {
        this.occupations = occupations;
    }

    public List<Location> getLocations() {
        return locations;
    }

    public void setLocations(List<Location> locations) {
        this.locations = locations;
    }

    public Health getHealth() {
        return health;
    }

    public void setHealth(Health health) {
        this.health = health;
    }

    public MaritalStatus getMaritalStatus() {
        return maritalStatus;
    }

    public void setMaritalStatus(MaritalStatus maritalStatus) {
        this.maritalStatus = maritalStatus;
    }
}
