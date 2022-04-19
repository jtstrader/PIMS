package com.pims.api.models;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonManagedReference;

import javax.persistence.*;
import java.util.List;

@Entity(name="Population")
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler"})
public class Population {
    @Id
    private String ssn;
    private String first_name;
    private String last_name;

    /*@OneToOne(mappedBy = "population")
    @JsonManagedReference
    private Occupation occupation;*/

    @OneToOne(mappedBy = "population")
    @JsonManagedReference
    private Location location;

    @OneToOne(mappedBy = "population")
    @JsonManagedReference
    private Health health;

    @OneToOne(mappedBy = "population")
    @JsonManagedReference
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

    /*public Occupation getOccupation() {
        return occupation;
    }

    public void setOccupation(Occupation occupation) {
        this.occupation = occupation;
    }*/

    public Location getLocation() {
        return location;
    }

    public void setLocations(Location location) {
        this.location = location;
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
