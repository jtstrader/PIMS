import { Component, OnInit, NgModule } from '@angular/core';
import { Subscription } from 'rxjs';
import { BrowserModule } from '@angular/platform-browser';
import { NgxChartsModule } from '@swimlane/ngx-charts';
//import { DeathRates, MaritalCounts, AverageSalary, PositionSalary } from './data';
import { AveragePositionSalaryByBusinessService } from '../services/average-position-salary-by-business.service';
import { CompanyAverageSalaryService } from '../services/company-average-salary.service';
import { MaritalCountByStateService } from '../services/marital-count-by-state.service';
import { DeathRatesByStateService } from '../services/death-rates-by-state.service';
import { IDeathRatesByState } from '../interfaces/ideath-rates-by-state';
import { IMaritalCountByState } from '../interfaces/imarital-count-by-state';
import { ICompanyAverageSalary } from '../interfaces/icompany-average-salary';
import { IAveragePositionSalaryByBusiness } from '../interfaces/iaverage-position-salary-by-business';
import { IPositionSalariesFormatted } from '../interfaces/iposition-salaries-formatted';

@Component({
  selector: 'app-graphs',
  templateUrl: './graphs.component.html',
  styleUrls: ['./graphs.component.css']
})
export class GraphsComponent implements OnInit {
  deathRates!: IDeathRatesByState[];
  maritalCount!: IMaritalCountByState[];
  companyAvgSalary!: ICompanyAverageSalary[];
  avgPositionSalary!: IAveragePositionSalaryByBusiness[];
  avgPositionSalaryFmt!: IPositionSalariesFormatted[];
  filteredAvgPositionSalary!: IAveragePositionSalaryByBusiness[];
  errorMessage: string = "";

  dr_sub!: Subscription;
  mc_sub!: Subscription;
  ca_sub!: Subscription;
  ap_sub!: Subscription;
  
  
  showXAxis = true;
  showYAxis = true;
  gradient = false;
  showLegend = false;
  showXAxisLabel = true;
  showYAxisLabel = true;
  timeline: boolean = true;
  
  
  Graph1X = 'State';
  Graph1Y = 'Death Rate';
  
  Graph2X = 'State';
  Graph2Y = 'Marital Counts';
  
  Graph3X = 'Company';
  Graph3Y = 'Average Salary';
  
  Graph4X = 'Company';
  Graph4Y = 'Salary';
  
  constructor(private deathRatesByState: DeathRatesByStateService,
    private maritalCountByState: MaritalCountByStateService,
    private companyAverageSalary: CompanyAverageSalaryService,
    private averagePositionSalary: AveragePositionSalaryByBusinessService) { 
    //Object.assign(this, { DeathRates1, MaritalCounts1, AverageSalary1, PositionSalary1 })
  }

  table: boolean[] = [false, false, false, false];
  
  ngOnInit(): void {
    this.dr_sub = this.deathRatesByState.getDeathRates().subscribe({
      next: drs => this.deathRates = drs,
      error: err => this.errorMessage = err
    });

    this.mc_sub = this.maritalCountByState.getMaritalCount().subscribe({
      next: mc => this.maritalCount = mc,
      error: err => this.errorMessage = err
    });

    this.ca_sub = this.companyAverageSalary.getTop10().subscribe({
      next: ca => this.companyAvgSalary = ca,
      error: err => this.errorMessage = err
    });

    this.ap_sub = this.averagePositionSalary.getAveragePositionSalariesFMT().subscribe({
      next: ap => this.avgPositionSalaryFmt = ap,
      error: err => this.errorMessage = err
    });
  }

  setTable(idx: number): void {
    this.table = this.table.map((_, index) => index == idx ? true : false);
  }

}