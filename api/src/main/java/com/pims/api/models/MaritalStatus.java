package com.pims.api.models;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import javax.persistence.*;
import java.util.List;

@Entity(name="marital_status")
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler"})
public class MaritalStatus {
    @Id
    private String ssn;
    private String partner_ssn;

    @OneToOne
    @PrimaryKeyJoinColumn
    @JsonBackReference
    private Population population;

    public MaritalStatus(){}

    public String getSsn() {
        return population.getSsn();
    }

    public void setSsn(String ssn) {
        this.getPopulation().setSsn(ssn);
    }

    public String getPartner_ssn() {
        return partner_ssn;
    }

    public void setPartner_ssn(String partner_ssn) {
        this.partner_ssn = partner_ssn;
    }

    public Population getPopulation() {
        return population;
    }

    public void setPopulation(Population population) {
        this.population = population;
    }
}
