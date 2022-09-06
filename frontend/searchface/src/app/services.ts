import {Injectable} from "@angular/core";
import {HttpClient, HttpErrorResponse, HttpHeaders, HttpParams} from "@angular/common/http";
import {catchError, Observable, Subject, throwError} from "rxjs";

@Injectable({providedIn: "root"})
export class Service{
  BACKENDURL = "http://localhost:5000"
  headers = new HttpHeaders()
    .set('Access-Control-Allow-Origin', '*');
  constructor(private httpClient:HttpClient) {
  }

  sendRefForFaceDetection(file:any): Observable<any> {
    return this.httpClient.post<any>(
      this.BACKENDURL + '/face/detect',
      file
    );
  }

  sendFaceSelection(selection:string): Observable<any> {
    let params = new HttpParams();
    params.append('id', selection)
    console.log("Send "  + selection)
    return this.httpClient.post<any>(
      this.BACKENDURL + '/face/select?id='+ selection,{params: params}
    );
  }

  sendGalleryPath(path:string): Observable<any> {
    return this.httpClient.post<any>(
      this.BACKENDURL + '/gallery/path',
      JSON.stringify(path)
    )
  }
  sendOutputPath(path:string): Observable<any> {
    return this.httpClient.post<any>(
      this.BACKENDURL + '/output/path',
      JSON.stringify(path)
    )
  }

  // @ts-ignore
  requestSearch(): Observable<any> {
    return this.httpClient.get(this.BACKENDURL + '/search/start')
  }

  stopSearch(): Observable<any>{
    return this.httpClient.get(this.BACKENDURL + '/search/stop')
  }
  requestSearchProgress(): Observable<any> {
    return this.httpClient.get(this.BACKENDURL + '/search/progress')
  }

  sendSettings(data: any): Observable<any>{
    return this.httpClient.post(this.BACKENDURL + '/settings',data)
  }
  handleError(error: HttpErrorResponse){
    console.log(error.error)
    return throwError(error)
  }

}
