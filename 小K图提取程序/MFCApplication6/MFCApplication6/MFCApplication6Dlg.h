
// MFCApplication6Dlg.h : 头文件
//

#pragma once

#include "Halconcpp.h"
#include "afxwin.h"
using namespace HalconCpp;


// CMFCApplication6Dlg 对话框
class CMFCApplication6Dlg : public CDialogEx
{
// 构造
public:
	CMFCApplication6Dlg(CWnd* pParent = NULL);	// 标准构造函数

// 对话框数据
	enum { IDD = IDD_MFCAPPLICATION6_DIALOG };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV 支持


// 实现
protected:
	HICON m_hIcon;
	HObject ho_image;
	HTuple hv_WindleHandle2,hv_width, hv_height;

	// 生成的消息映射函数
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
public:
	afx_msg void OnBnClickedButton1();
	afx_msg void OnBnClickedSmallK();

	HTuple hv_WindleHandle;

	bool GetLabelImageInfo(const HObject hCatSearchImage,
		const int nLabelPeriod, const int nLabelRow, const int nLabelCol,
		int& nChannel,
		BOOL& bStartConfidence,
		HTuple& hStartRow, HTuple& hRowSpace,
		HTuple& hStartCol, HTuple& hColSpace,
		HObject& hCatSingleLabelImage);
	
	int k_rows, k_cols;//这里之所以定义为全局，是为了多个函数共有
	int k_pers, nChannel;
	BOOL bStartConfidence;

	HTuple hStartRow, hRowSpace, hStartCol, hColSpace;
	HObject hCatSingleLabelImage;

	CEdit Edit_K_pers;
	CEdit Edit_K_rows;
	CEdit Edit_K_cols;
	CStatic m_Label_5;
	CStatic m_label_6;
	CStatic m_label_7;
	CStatic m_label_8;
	CStatic m_label_9;
	CStatic m_label_10;
};


